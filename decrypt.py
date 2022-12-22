import os 
from cryptography.fernet import Fernet

files = []
# we need to exclude our mal.py filee
for file in os.listdir():
    if file == "mal.py" or file =="thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key" , "rb" ) as key:
    secret_key = key.read()


secret = "noob"
seceret_p = input("Enter the secret phase\n")    

if secret==seceret_p:
    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()
# display the encrypted data...
        con_decrypt = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(con_decrypt)  
        print("Decryped")  
else:
    print("wrong key")

