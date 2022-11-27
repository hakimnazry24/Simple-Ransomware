import os
from cryptography.fernet import Fernet
import time

secretKey = 48472938489

# get right input from users to continue decryption
inputtedKey = int(input("Enter the secret key: "))
while inputtedKey != secretKey:
    print("WRONG KEY!!! TRY AGAIN")
    inputtedKey = int(input("Enter the secret key: "))

# add all files in directory to files list
files = []
for file in os.listdir():
    if file == 'encrypt.py' or file == 'decrypt.py' or file == 'encryptionKey.key':
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

# read secret key from encryptionKey.key file
with open("encryptionKey.key", 'rb') as file:
    secretKey = file.read()

# decryption of file
for file in files:
    with open(file, 'rb') as readFile:
        content = readFile.read()
    with open(file, 'wb') as writeFile:
        decrypted_content = Fernet(secretKey).decrypt(content)
        writeFile.write(decrypted_content)

print("ALL OF YOUR FILES HAS BEEN DECRYPTED")
