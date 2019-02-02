#!/usr/bin/python3

#blockExplorer_1.py
# Stake calculations from a Neblio address
# Crontab instruction to run once a day at 23:55:
# 59 23 * * * /usr/bin/python3 /home/pi/accountant/blockExplorer_1.py

'''
API
getbalance (/ext/getbalance/hash) 
Returns current balance of given address 
explorer.nebl.io/ext/getbalance/<address>
'''

import requests, json
import time


def get_address():
  global address
  fileobj= open('/home/pi/accountant/address.txt', 'rt')
  address= fileobj.read()
  address= address.strip('\n') # Strips the new line symbol from the end of the address '\n'
  # print('Address:', address)
  fileobj.close()
  

def get_last_balance():
  global last_balance
  fileobj= open('/home/pi/accountant/balance.txt', 'rt')
  b= fileobj.read()
  last_balance=float(b)
  print('Last balance:',last_balance)
  fileobj.close()


def get_NEBL_balance():
  URL_BAL= "http://explorer.nebl.io/ext/getbalance/" + address
  try:
    r= requests.get(URL_BAL)
    b= json.loads(r.text)
    new_balance= float(b)
    if new_balance > last_balance:
      timestamp = int(time.time())
      stake = new_balance - last_balance
      print('New balance:',new_balance,'Timestamp:',timestamp)
      print('Stake:',stake)
      write_new_balance(new_balance)
      write_account(timestamp, stake, new_balance)
    else:
      print('No recent stakes')
  except requests.ConnectionError:
    print("Error querying Block Explorer API")


def write_new_balance(new_balance):
  new_balance= str(new_balance)
  fileobj= open('/home/pi/accountant/balance.txt', 'wt')
  fileobj.write(new_balance)
  fileobj.close()
  print('Saved new balance to balance.txt')
  
def write_account(timestamp, stake, new_balance):
  localtime = time.asctime(time.localtime(time.time()))
  timestamp= str(timestamp)
  stake= str(stake)
  new_balance= str(new_balance)
  update= localtime + "," + timestamp + "," + stake + "," + new_balance
  fileobj= open('/home/pi/accountant/account.txt', 'a')
  fileobj.write(update)
  fileobj.write("\n")
  fileobj.close
  print('Saved localtime, timestamp, stake and the new balance to account.txt')
  

get_address()
get_last_balance()
get_NEBL_balance()

'''
# for testing
while True:
  get_NEBL_balance()
  time.sleep(3600)

'''

