import hashlib
import time

filename = "inbtween.txt"
prev_hash=""
prev_num = 0
pr_d=""

def sha256_hash(data):
	sha256 = hashlib.sha256()
	sha256.update(data.encode('utf-8'))
	hashed_data=sha256.hexdigest()
	return hashed_data

def read_last_line(filename):
	with open(filename, 'r')as file:
		lines=file.readlines()
		num_lines = len(lines)
		data=lines[-3].strip()
		hash_data=lines[-2].strip()
	return data,hash_data,num_lines
	
def write(data, filename):
	with open(filename, 'a')as file:
		file.write(f"{data}\n")
			

while True:
	data,hash_data,num=read_last_line(filename)
	
	if num != prev_num or hash_data!=prev_hash or data!=pr_d:
		if sha256_hash(data) != hash_data:
			print('The command bellow is considered invalid!')
			write(0,"feedback.txt")
		else:
			write(data, "commandRecorder.txt")
			write(1,"feedback.txt")
		print(data)
		print(hash_data,"\n")
		prev_num,prev_hash,pr_d = num,hash_data,data

	time.sleep(1)
