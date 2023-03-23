# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:33:32 2020

@author: lockd

            
                            LINEAR SEARCH
Searching for the given number one by one in the given list

                            BINARY SEARCH
1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid index.
3. Else if x is greater than the mid element, then x can only lie in the right 
(greater) half subarray after the mid element. Then we apply the algorithm again 
for the right half.
4. Else if x is smaller, the target x must lie in the left (lower) half. So we 
apply the algorithm for the left half.
                            
                              
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

def linear_search(l,x):     #L is the list and x is the number to be searched
    
    flag = 0    #Flag = 0 means number not found
    count = 0   #Count to check the position of x or in how many iterations, x is found
    
    for i in l:
        count+=1
#Now if x=3 and it's not in list, still it will check all the elements of list
#So linear search is not an efficient searching algorithm
#To make it efficient, using if i>x
        if(i>x):
            break
        else:
            if(i==x):
                print("Yes I found ",x,'at position ',count)
                flag = 1
                break
    
    if(flag == 0):
        print(x,"Not found")
#For searching the number we can use the built in function also: if x in l , like sort for sorting.


def binary_search(l,x):
    
    first_pos = 0   #First Index of list
    last_pos =  len(l)-1    #Last index of list
    
    flag = 0    #Flag=0 means x is not found
    
    count = 0   #Count to check in how many iterations, x is found
    
    while(first_pos<=last_pos):
        count+=1
        mid = (first_pos + last_pos)//2
        if(l[mid] == x):
            print('Yes, I found ',x,'at position ',mid+1)   #mid+1 considers index0 = 1
            print('I found it in ',count,'iterations')
            flag == 1
            break
        else:
            if(x>l[mid]):
                first_pos = mid+1
            if(x<l[mid]):
                last_pos = mid-1
    
    if(flag == 0):
        print(x,"Not found")
        


l = random_list()

n = int(input("Enter the number you want to search: "))

linear_search(l,n)
binary_search(l,n)   
