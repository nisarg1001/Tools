#!/usr/bin/python

import ftplib

def anologin(host):
	try:
		ftp = ftplib.FTP(host)
		ftp.login('anonymous' , 'anonymous')
		print("[*] " + host + " FTP anonymous logon succeeded")
		ftp.quit()
		return True
	except(Exception , e):
		print("[-] " + host + " FTP anonymous logon failed")


host = "192.168.29.196"

anologin(host)
