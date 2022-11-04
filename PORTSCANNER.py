#DEPRACTED THIS VERSION DOES NOT WORK SEE portscanner2.py

import socket as sk
for port in range (1,1024):
    try:
        s=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
        s.settimeout(1001)
        s.connect(('127.0.0.1',port))
        print '%d:OPEN' % (port)
        s.close
    except: continue

#DEPRACTED THIS VERSION DOES NOT WORK SEE portscanner2.py

print("#DEPRACTED THIS VERSION DOES NOT WORK SEE portscanner2.py")
