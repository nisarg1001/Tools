#!/usr/bin/python

import crypt

def crackpass(passwd):
	salt = passwd[0:2]
	f = open('dictionary.txt' , 'r')
	for line in f.readlines():
		crypted = crypt.crypt(line.strip('\n') , salt)
		if(crypted == passwd):
			print("[*] Password found : " + line)
			quit()


def main():
	passfile = open('passwords.txt' , 'r')
	for password in passfile.readlines():
		if(":" in password):
			user = password.split(':')[0]
			passwd = password.split(':')[1].strip(' ').strip('\n')
			
			print("[*] cracking password for : " + user)
			crackpass(passwd)
	print("[-] Password not found in list")
main()
