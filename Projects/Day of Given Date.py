"""
Created on Thu Dec 17 21:02:43 2020

@author: lockd

I have to tell that given date falls on which day of week
IMPORTANT POINTS
Months till July(07): 
    Odd months have 31 days and Even months have 30 days
Months from August(08):
    Odd months have 30 days and Even months have 31 days
    
APPROACH
Input Year 
Input month
Input date
Check If date is correct or not i.e suppose user has entered 31 date \
    for month September
Find day
Print day

"""

import calendar

def check_leap_year(y):
    if y%4==0 and y%100!=0 or y%100==0 and y%400==0:
        return True
    else:
        False

def check_valid_date(d,m,y,leap):
    if leap:
        if m==2:
            if d<30:
                return True
            else:
                return False
        else:
            if m>=1 and m<=8: #Months till July
                if m%2==1:  #Odd Months
                    if d<=31:
                        return True
                    else:
                        return False
                else: #Even Months
                    if d<=30:
                        return True
                    else:
                        return False
            else: #Months from August
                if m%2==1:  #Odd Months
                    if d<=30:
                        return True
                    else:
                        return False
                else: #Even Months
                    if d<=31:
                        return True
                    else:
                        return False 
                    

def find_day(day_index):
    days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = days_list[day_index]
    return day
    
while(1):
    y = int(input('Enter year (1970-2020): '))
    if y<1970:
        print('Please enter year starting from 1970')
    else:
        break

while(1):
    m = int(input('Enter month (1-12): '))
    if m>0 and m<13:
        break
    else:
        print('Enter valid month')

while(1):
    d = int(input('Enter date (1-31): '))
    if d>0 and d<32:
        break
    else:
        print('Enter a valid date')

leap = check_leap_year(y)

if check_valid_date(d,m,y,leap):
    day_index = calendar.weekday(y,m,d)
    day = find_day(day_index)
    print('Day on date ',d,'/',m,'/',y,' is ',day)

else:
    print('You entered wrong date')