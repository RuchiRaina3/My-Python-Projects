# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:21:09 2020

@author: lockd


                   SUBSTITUTION CIPHER OF A GIVEN FILE 

"""

import string

all_letters = string.ascii_letters

dict1 = {}
key = int(input("Enter key: "))

for i in range(len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]

f1 = open("D:\OneDrive\Documents\Original.txt")
f2 = open("D:\OneDrive\Documents\Encrypted.txt","r+")

data = ''

while(True):    #True so that while condition gets executed
    c = f1.read(1) 
    
    if not c:      
        break;
    if c in dict1:
        data = dict1[c]
    else:
        data = c
    f2.write(data)
    print(data, end='')
print()

f1.close()
f2.close()

f2 = open("D:\OneDrive\Documents\Encrypted.txt","r+")
f3 = open("D:\OneDrive\Documents\Recovered.txt","r+")

#Recovering Text
dict2 = {}      



for i in range(len(all_letters)):
    dict2[all_letters[i]] = all_letters[(i-key)%len(all_letters)]

while(True):    #True so that while condition gets executed
    c = f2.read(1) 
    
    if not c:      
        break;
    if c in dict2:
        data = dict2[c]
    else:
        data = c
    f3.write(data)
    print(data, end='')  
print()

f2.close()
f3.close()
    