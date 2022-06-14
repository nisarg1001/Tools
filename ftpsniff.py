#!/usr/bin/python

import optparse
from scapy.all import *

def main():
	parser = optparse.OptionParser("Usage of the program : -i <interface>")
	parser.add_option('-i' , dest='interface' , type="string" , help="specify interface")
	(option , args) = parser.parser_args()
	if(option.interface == None):
		print(parser.usage)
		exit(0)
	else:
		conf.interface = option.interface

	try:
		sniff(filter="tcp port 21" , prn=ftpsniff)
	except KeyboardInterrupt:
		exit(0)
