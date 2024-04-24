import hashlib
import time
filename = "inbtween.txt"

def sha256_hash(data):
	sha256 = hashlib.sha256();
	sha256.update(data.encode('utf-8'))
	hashed_data=sha256.hexdigest()
	return hashed_data

def write(data, hashed, filename):
	with open(filename, 'a')as file:
		file.write(f"{data}\n")
		file.write(f"{hashed}\n\n")
			
def read_last_line(filename):
	data=''
	with open(filename, 'r')as file:
		lines=file.readlines()
		if len(lines) != 0:
			data=lines[-1].strip()
	return data

while 1==1:
	data = input("Enter the data to hash using SHA-256:")
	hashed_data = sha256_hash(data)
	print("SHA-256 Hash:",hashed_data)
	write(data, hashed_data, filename)
	time.sleep(10)
	num = read_last_line("feedback.txt\n")
	if num=='1':
		print("Succesfully sent message.\n")
	else:
		print("Message delivery was failed. Please resent")
