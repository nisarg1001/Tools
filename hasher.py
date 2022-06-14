#!/usr/bin/python

import hashlib
import crypt

crypted = crypt.crypt("admin" , "HG")
print("Crypted = " + crypted)

hashvalue = input("Enter the string to hash ")
hashed = hashvalue.encode('utf-8')
md5digest = hashlib.md5(hashed.strip()).hexdigest()
print("md5digest : " + md5digest)

hashobj1 = hashlib.md5()
hashobj1.update(hashvalue.encode())
print(hashobj1.hexdigest())

hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())
print(hashobj2.hexdigest())

hashobj3 = hashlib.sha224()
hashobj3.update(hashvalue.encode())
print(hashobj3.hexdigest())

hashobj4 = hashlib.sha256()
hashobj4.update(hashvalue.encode())
print(hashobj4.hexdigest())

hashobj5 = hashlib.sha512()
hashobj5.update(hashvalue.encode())
print(hashobj5.hexdigest())


