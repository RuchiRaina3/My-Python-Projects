# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:09:57 2020

@author: lockd

       ANAGRAMS LOGIC 2: If the sorted strings are equal, then are ANAGRAMS

"""

s1 = input("Enter the first string:  ")
s2 = input("Enter the second string:  ")

print(sorted(s1))
print(sorted(s2))

if sorted(s1)==sorted(s2):
    print('Anagrams')
else:
    print('Not Anagrams')