# Simple analysis of BlockExplorer_1.py results
# Fields are: date,time,timestamp,balance,stake

import csv

f = open('account.txt', 'r')

with f:
  reader = csv.DictReader(f)
  total_stake= 0
  num_days= 0
  dayList= []
  for row in reader:
    dayList.append(row)
    num_days= num_days +1
    day_stake= float(row['stake'])
    total_stake= total_stake + day_stake
    
    #total_stake= round(total_stake,8)
    #print(row['date'], row['time'], row['timestamp'], row['balance'], row['stake'])


dayListReversed= list(reversed(dayList))

print('\nNumber of days:', num_days)
total_stake= round(total_stake,8)
print('Total stakes:', total_stake)
daily_average= round(total_stake/num_days,8)
print('Daily average:', daily_average)
last_balance= float(dayListReversed[0]["balance"])
expected= (last_balance/10)/365
expected= round(expected,8)
print('Expected (per last balance):', expected)

print()
print("\nLAST 30 DAYS")
for row in dayListReversed[0:30]:
  print(row['date'], row['time'], row['timestamp'], row['balance'], row['stake'])


