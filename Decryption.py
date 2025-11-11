#!/usr/bin/env python3

import os
from cryptography.fernet import ferent

files = []


for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key" or file == "Decryption.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    sceretkry = key.read()


for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = ferent (key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

print("All Your Files Are Decrypted")






