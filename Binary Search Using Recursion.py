# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:11:13 2020

@author: lockd

        Binary Search Using Recursion
"""


import random

def random_list():  #To generate a list of random numbers
    l = []
    for i in range(100):   #Runs for 100 times: 0 from 99
        r = random.randint(0,1000)  #Incuding 1000
        if r not in l:
            l.append(r)     
    l.sort()
    print(l)
    
    return l

def binary_search(l,x,first_pos,last_pos):
    #Base Case
    if first_pos==last_pos:
        if(l[first_pos]==x):
            return first_pos
        else:
            return -1
    else:
        #Divide The list into halves
        mid = (first_pos+last_pos)//2
        
        if l[mid]==x:
            return mid
        elif x>l[mid]:
           return binary_search(l,x,mid+1,last_pos)
        else:
           return  binary_search(l,x,first_pos,mid-1)   
            

l = random_list()

n = int(input("Enter the number you want to search: "))
index = binary_search(l,n,0,len(l)-1)


if(index==-1):
    print(n,' not found')
else:
    print(n,' is found at position ', index+1)