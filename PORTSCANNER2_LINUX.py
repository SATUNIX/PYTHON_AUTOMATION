#   Author = Anthony
#   Date = 4/11/2022
#   Version 1.3
#   Port Scanner Python for Linux Systems 
#   © Tritium Cyber Defence 2022 No Rights Reserved
#   All works submitted as my own

import sys
import os
import socket
import time
from datetime import datetime

#Start intro text
print("_" * 75)
print("\n\tWELCOME TO THE TRITIUM PORT SCANNER\n")

size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("T", end=' ')
    print(" ")

text = 'PORT SCAN VERSION 1.1'

print("_" * 75)

time.sleep(2)

#PROGRAM CONFIGURATION AND INFORMAITON
print("\n", ascii(text))
os.system("ip congfig")
time.sleep(0.5)
print("\nYour own Linux IP configurations are listed above :) \n")
print("_" * 75)
target = input(str("\nEnter Target Address(IPv4): "))
print("_" * 75)

#SCAN PRINTS
print("\nScanning Target IP: " + target)
time.sleep(0.2)
print("Scanning Start Time: " + str(datetime.now()))
time.sleep(0.2)
print("This may take some time... Grab a coffee: ")
time.sleep(0.2)
print("_" * 75)

try:
    #scan every port on the target ip
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        #return the open ports
        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()
#PROGCLOSE       
except KeyboardInterrupt:
    print("\n EXITING NOW: \n")
    sys.exit()
    
except socket.error:
    print("\Host Non Responsive")
    print("Try again on new address")
    sys.exit()
#PROGCLOSE
print("Thanks for Scanning :)")