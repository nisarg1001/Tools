#!/usr/bin/python

from socket import *

def findBanner(ip , port):
	try:
#		print(port)
		sock = socket(AF_INET , SOCK_STREAM)
#		print("ASDf")
		sock.connect((ip , port))
#		print("asdf")
		setdefaulttimeout(2)
#		print("asdf")
		banner = sock.recv(1024)
		return banner
	except:
#		print("ASDF")
		return

def main():
	#ip = input("Enter the IP to get the banner ")
	ip = "192.168.29.196"
	for port in range(1 , 100):
		banner = findBanner(ip , port)
		if(banner):
			print("[*]" + ip + "/" + str(port) + " : " + str(banner))

main()
