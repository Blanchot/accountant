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
    dayList= dayList.append(row)
    num_days= num_days +1
    day_stake= float(row['stake'])
    total_stake= total_stake + day_stake
    
    #total_stake= round(total_stake,8)
    #print(row['date'], row['time'], row['timestamp'], row['balance'], row['stake'])

print('\nNumber of days:', num_days)
total_stake= round(total_stake,8)
print('Total stakes:', total_stake)
daily_average= round(total_stake/num_days,8)
print('Daily average:', daily_average)

print()
dayListReversed= list(reversed(dayList))

for row in dayListReversed:
  print(row['date'], row['time'], row['timestamp'], row['balance'], row['stake'])


'''
  for row in reader:
    print(row['date'], row['time'], row['timestamp'], row['balance'], row['stake'])
'''

