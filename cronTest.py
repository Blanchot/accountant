#!/usr/bin/python3
# cronTest.py
# Python script test for crontab
# NOTE: First create cronTest.txt by hand
# Crontab instruction: 
# 

import time

localtime = time.asctime(time.localtime(time.time()))

fileobj= open('cronTest.txt', 'a')
fileobj.write(localtime)
fileobj.close

print("Local current time :", localtime)
