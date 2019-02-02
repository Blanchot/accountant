#blockExplorer_1.py
# Stake calculations from a Neblio address

'''
API
getbalance (/ext/getbalance/hash) 
Returns current balance of given address 
explorer.nebl.io/ext/getbalance/<address>
'''

import requests, json
import time
from time import time


def get_address():
  global address
  fileobj= open('address.txt', 'rt')
  address= fileobj.read()
  address= address.strip('\n') # Strips the new line symbol from the end of the address '\n'
  # print('Address:', address)
  fileobj.close()
  

def get_last_balance():
  global last_balance
  fileobj= open('balance.txt', 'rt')
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
      tijd = int(time())
      stake = new_balance - last_balance
      print('New balance:',new_balance,'Timestamp:',tijd)
      print('Stake:',stake)
      write_new_balance(new_balance)
      write_account(tijd, stake, new_balance)
    else:
      print('No recent stakes')
  except requests.ConnectionError:
    print("Error querying Block Explorer API")


def write_new_balance(new_balance):
  new_balance= str(new_balance)
  fileobj= open('balance.txt', 'wt')
  fileobj.write(new_balance)
  fileobj.close()
  print('Saved new balance to balance.txt')
  
def write_account(tijd, stake, new_balance):
  tijd= str(tijd)
  stake= str(stake)
  new_balance= str(new_balance)
  update= tijd + "," + stake + "," + new_balance
  fileobj= open('account.txt', 'a')
  fileobj.write(update)
  fileobj.close
  print('Saved time, stake and the new balance to account.txt')
  

get_address()
get_last_balance()
#get_NEBL_balance()

while True:
  get_NEBL_balance()
  time.sleep(3600)
 

