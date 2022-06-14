#!/usr/bin/python

import subprocess

def changeMac(interface , mac):
	subprocess.call(["sudo","ifconfig",interface,"down"])
	subprocess.call(["sudo","ifconfig",interface,"hw","ether",mac])
	subprocess.call(["sudo","ifconfig",interface,"up"])

def main():
	interface = input("Enter the interface ")
	#interface = "eth0"
	new_mac_address = input("Enter the new mac address ")
	before_change = subprocess.check_output(["ifconfig", interface])
	changeMac(interface , new_mac_address)
	after_change = subprocess.check_output(["ifconfig", interface])
	if(before_change == after_change):
		print("[-] Mac address not changed")
	else:
		print("[+] Mac address is changed")
#	index= (str(before_change).strip(' ')).find('ether')
#	print(str(before_change)[226:243])
#	print(after_change)

main()
