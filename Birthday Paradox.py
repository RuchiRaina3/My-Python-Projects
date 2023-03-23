# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:19:29 2020
@author: lockd

Check within a randomly genetrated 50 samples of 
birthdays, how many are common.

"""

import random
import datetime

birthday = []

i = 0
while(i<50):
    #Generating year
    year = random.randint(1898,2020)
    #Beacuse oldest person ever lived aged 122 years and 2020 - 122 = 1898
    
    #Checking for leap year
    if(year%4==0 and year%100==0 or year%400==0):
        leap = 1
    else:
        leap = 0
    
    #Generating months
    month = random.randint(1,12)
    
    #Generating days
    if(month==2 and leap==1):
        day = random.randint(1,29)
    elif(month==2 and leap==0):
        day = random.randint(1,28)
    elif(month==1 or month==5 or month==7 or month==8 or month==10 or month==12):
        day = random.randint(1,31)
    else:
        day = random.randint(1,30)
        
    dd = datetime.date(year,month,day)
    dayOfYear = dd.strftime("%j") 
    birthday.append(dayOfYear)
    
    i = i+1

birthday.sort()

i = 0
while(i<50):
    print(birthday[i])
    i = i+1
                    



