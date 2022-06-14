#!/usr/bin/python

from urllib.request import urlopen
import hashlib

sha1hash = input("[*] Enter the hash value of password ")
passlist = str(urlopen('https://raw.githubusercontent.com/iryndin/10K-Most-Popular-Passwords/master/passwords.txt').read() , 'utf-8')

for password in passlist.split('\n'):
	hashguess = hashlib.sha1(bytes(password , 'utf-8')).hexdigest()
	if(hashguess == sha1hash):
		print("[+] The password is : " + password)
		quit()
	else:
		print("[-] Password guess : " + password + " is incorrect")

print("Password is not in list")
