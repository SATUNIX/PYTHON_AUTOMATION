#!/usr/bin/python
#FROM THE RTFM NOTETHAT I NEED TO ADD IN VARIABLES AND USR INPUT FOR VERSATILITY AND SPEED FOR THE SPOOFING PKGs
import smtplib,string
import os, time

os.sysyem("/etc/init.d/sendmail.start")
time.sleep(5)

HOST ='localhost'
SUBJECT = "TRITIUM SPOOF TEST"
TO = "target@you.com"
FROM = "spoof@spoof.com"
TEXT = "message body"
BODY = string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject %s" % SUBJECT,
    "",
    TEXT
    ), "\r\n")
server = smtplib.SMTP(HOST)
server.sendmail (FROM, [TO], BODY)
server.quit()

time.sleep(5)
os.system("/etc/init.d/sendmail stop")

