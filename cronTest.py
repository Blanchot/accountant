#!/usr/bin/python3

# cronTest.py
# Python script test for crontab
# NOTE: First create cronTest.txt by hand
# Crontab instruction to run every minute: 
# * * * * * /home/pi/work/accountant/cronTest.py

import time

localtime = time.asctime(time.localtime(time.time()))

# note: need to define full pathway below otherwise it creates cronTest.txt in home directory
fileobj= open('/home/pi/work/accountant/cronTest.txt', 'a')
fileobj.write(localtime)
fileobj.write('\n')
fileobj.close

#print("Local current time :", localtime)
