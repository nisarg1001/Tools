#!/usr/bin/python

import os
import socket
import sys

def retbanner(ip , port):
	try:
		sock = socket.socket()
		socket.setdefaulttimeout(2)
		sock.connect((ip,port))
		banner = sock.recv(1024)
		return banner
	except:
		return

def checkvulns(banner , file):
	f = open(file , "r")
	for line in f.readlines():
		if(str(line.strip('\n')) in str(banner)):
			print('[+] server is vulnerable' + str(banner))

def main():
	if(len(sys.argv) == 2):
		filename = sys.argv[1]
		if(not os.path.isfile(filename)):
			print('[-] file does not exist')
			exit(0)
		if(not os.access(filename , os.R_OK)):
			print('[-] access denied')
			exit(0)
	else:
		print("[-] Usage: " + str(sys.argv[0]) + "<vuln_filename>")
		exit(0)
	portlist = [21,22,25,80,110,135,139,445,443]
	ip = "192.168.29.196"
	for port in portlist:
		banner = retbanner(ip,port)
#		print(banner)
		if(banner):
			print("[+]" + ip + "/" + str(port) + " : " + str(banner))
			checkvulns(banner ,filename)

main()
