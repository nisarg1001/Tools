#!/usr/bin/python

import pexpect

PROMPT = ['# ' , '<<< ' , '> ', '\$ ']

def send_command(child ,command):
	child.sendline(command)
	child.expect(PROMPT)
	print(child.before) #print the output after execution of command

def connect(user , host , password): #following the flow of ssh connection
#	ssh_newkey = "Are you sure you want to continue connecting"
	conn_str = "ssh " + user + "@" + host
	child = pexpect.spawn(conn_str)
	ret = child.expect([pexpect.TIMEOUT , '[P|p]assword'])
#	we can remove this lines bcz connection is not asking for the confirmation
#	if(ret == 0):
#		print("[-] error in connecting")
#		return
#	if(ret == 1):
#		child.sendline("yes") #means ssh_newkey has been prompted so send yes
#		ret = child.expect([pexpect.TIMEOUT , '[P|p]assword'])
#		if(ret == 0):
#			print("[-] error in connecting")
#			return
	child.sendline(password)
	child.expect(PROMPT)
	return child

def main():
	host = input("[+] Enter the host to connect ")
	user = input("[+] Enter the user ")
	password = input("[+] Enter the password ")
	child = connect(user , host , password)
	send_command(child , 'ls;ps')

main()
