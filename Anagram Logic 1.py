# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:10:17 2020

@author: lockd

         ANAGRAMS LOGIC 1: Sum of all the ASCII characters is same for ANAGRAMS
Works even if the first letter of both the strings is capital.

"""

s1 = input("Enter the first string:  ")
s2 = input("Enter the second string:  ")

sum1 = 0
for i in s1:
    sum1 = sum1 + ord(i)    
print(sum1)

#With while loop
"""
i = 0
while(i<len(s1)):
    sum1 = sum1 + ord(s1[i])
    i = i+1
"""    

sum2 = 0
for i in s2:
    sum2 = sum2 + ord(i)    
print(sum2) 

if sum1==sum2:
    print('Anagrams')
else:
    print('Not Anagrams')
