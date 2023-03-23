# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 20:57:14 2020

@author: lockd

                        LOTTERY SIMULATION
Price of 1 bet is Rs.100 and winning amount is Rs.1000.
account variable keeps the track of the net money you have.    
User will be asked for how many times he want to play.    
Finally, a graph will be plotted to have a look at the patter of net profit or loss                
"""

import random
import matplotlib.pyplot as plt

account = 0
x = []
y = []

n = int(input('How many times do you want to play? '))
for i in range(n):
    x.append(i+1)
    bet = random.randint(1,10)
    lucky_draw = random.randint(1,10)
    print(bet, lucky_draw)
    if bet == lucky_draw:
        print('Won')
        account = account + 1000 - 100
    else:
        print('Lost')
        account = account - 100
    y.append(account)    
print()
print('Net amount = ', account)

plt.xlabel('Times Played')
plt.ylabel('Account')
plt.plot(x,y)

