#Author = Anthony Grace
#Date = 03-11-22
#Program = NETWATCH V2.1
#Purpose = Scan an entire network for open ports
#Display the IP Address on the network and their ports
#GH = https://github.com/SATUNIX

import os
import socket
import multiprocessing
import subprocess
import time
import sys
from datetime import datetime

def pinger(job_q, results_q):
    DEVNULL = open(os.devnull, 'w')
    while True:
        ip = job_q.get()
        if ip is None:
            break
        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass
def get_my_ip():
    """
    Find my IP address
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
def map_network(pool_size=255):
    ip_list = list()
    # get my IP and compose a base like 192.168.1.xxx
    ip_parts = get_my_ip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
    # prepare the jobs queue
    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()
    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()
    # cue the ping processes
    for i in range(1, 255):
        jobs.put(base_ip + '{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()
    # collect the results
    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list

if __name__ == '__main__':

    print('Mapping The LAN')
    time.sleep(1)
    print("This can take a while depending on the network size and amount of subnetting")
    lst = map_network()
    print(lst)
    print("\nHere is the addresses on the network^")
    print("_" * 50)
#Start intro text
print("\nLAN MAP OF ADDRESSES: ")

time.sleep(0.2)

#append list into a string
iplist = []
ip = lst
iplist.append(ip)
ip = lst

# KEEP THIS, the list is reffered to as string from now on ******
string = lst
#KEEP ***********************************************************

# output ip list

print(string)

text = 'PORT START:'
time.sleep(0.2)

#PROGRAM CONFIGURATION AND INFORMAITON
print("\n", ascii(text))

print("_" * 50)
startp = int(input("\nEnter Port Number Scan Start: "))
endp = int(input("\nEnter Port Number Ending for scan: "))
print("_" * 50)

#SCAN PRINTS
print("\nScanning The Target IPs: ")
print(string)
print("Scanning ports " , startp , " Through to " , endp)

time.sleep(0.2)
print("Scanning Start Time: " + str(datetime.now()))
time.sleep(0.2)
print("This may take some time... Grab a coffee: ")
time.sleep(0.2)
print("_" * 50)

try:
    for string in lst:
    #scan every port on the target ip
        for port in range(startp, endp):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

        #return the open ports
            result = s.connect_ex((string,port))
            if result == 0:
                print("[*] Port {portn} is open on IPv4 Address: {ipn}".format(portn = port , ipn = string))
            s.close()
#PROGCLOSE
except KeyboardInterrupt:
    print("\n EXITING NOW: \n")
    sys.exit()

except socket.error:
    print("\Host Non Responsive")
    print("Try again on new address")
    sys.exit()


#define the variables for tcpdump settings
#Below block pulls configs from above and uses them in a tcpdump command to gain info on the ports and hosts from the return block
#return block on line 127
print("_"*50)
os.system("ip a")
p = portn
h = ipn
print("_"*50)
i = input("Enter Interface to use: ")
#command system call
cmd = "sudo tcpdump -v -nn -s0 -i{0} port {1} host {3}".format(i,p,h)
os.system(cmd)

#PROGCLOSE