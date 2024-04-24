import hashlib
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
			

while 1==1:
	data = input("Enter the data to hash using SHA-256:")
	hashed_data = sha256_hash(data)
	print("SHA-256 Hash:",hashed_data)
	write(data, hashed_data, filename)
