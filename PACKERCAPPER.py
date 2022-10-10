#!/usr/bin/python
import os

inter=input("select interface [eth0,wlan0,etc]") #user input needed to select interface

os.system("tcpdump -i %s -XX -w out.pcap", %inter) #capture packets on interface input and write to pcap file
os.system("tcpdump -i %s -c 50 -tttt 'udp and port 53", %inter) #capture 50 DNS packets and print the timestamp
