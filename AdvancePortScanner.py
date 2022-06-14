#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connscan(tgtHost , tgtPort):
	try:
		sock = socket(AF_INET , SOCK_STREAM)
		sock.connect((tgtHost , tgtPort))
		print('[+] %d/tcp open' % tgtPort)
	except:
		print('[-] %d/tcp closed' %tgtPort)
	finally:
		sock.close()

def portscan(tgtHost , tgtPort):
	try:
		tgtIP = gethostbyname(tgtHost) #return IP if IP is input else return IP of host
	except:
		print('Unknown host %s') %tgtHost
	try:
		tgtname = gethostbyaddr(tgtIP)
		#return a list [domainname , [] , IP]
		print('[+] Scan result for : ' + tgtname[0])
	except:
		print('[+] Scan result for : ' +tgtIP)
	setdefaulttimeout(1)
	for tgtport in tgtPort:
		t = Thread(target=connscan, args=(tgtHost , int(tgtport)))
		t.start()
def main():
	parser = optparse.OptionParser("Usage of program :  " + "-H <target_host> -p <target_port>")
	parser.add_option('-H' , dest='tgtHost' , type='string' , help='specify target host')
	parser.add_option('-p' , dest='tgtport' , type='string' , help='specify target port seperated by coma')
	(options, args) = parser.parse_args() 
	tgtHost = options.tgtHost #used to fetch the input given by user in cmd line
#	print(options.tgtHost) #print the value specified with -H
#	print(options.help)
#	print(args)
	tgtport = str(options.tgtport).split(',')
	if((tgtHost == None) | (tgtport == None)):
		print(parser.usage)
		exit(0)
	portscan(tgtHost , tgtport)

main()

