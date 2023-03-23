# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:56:17 2020

@author: lockd

                            FLAMES
                            
"""

import string

def removing_similar_letters(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                c = l1[i]
                l1.remove(c)
                l2.remove(c)
                l = l1+['*']+l2 #['*'] as boundary between names
                return (l,True)
    l = l1+['*']+l2 #When no common letter is found
    return(l,False)
                
p1 = input('Enter the name of 1st person: ') 
p1 = p1.lower() #Suppose names are Amit and Priya. Computer will treat A and a differently
p1 = p1.replace(' ','') #Suppose one person write his full name and other person not. So space should'nt be considered

p2 = input('Enter the name of 2nd person: ') 
p2 = p2.lower()
p2 = p2.replace(' ','') #Replacing space with empty character/nothing

l1 = list(p1)   #List because we can do alot of things with list
l2 = list(p2)

again = True    #again for executin the while loop until all letters of name1 are compared
while(again):
    returned = removing_similar_letters(l1,l2)
    l = returned[0]
    star_index = l.index('*') #For list slicing
    l1 = l[:star_index]
    l2 = l[star_index+1:]
    again = returned[1]

#Now the names of nothing in common
count = len(l1) + len(l2)

flames = ['FRIENDS','LOVE','AFFECTION','MARRIAGE','ENEMIES','SIBILING']
#Cutting Part
while len(flames)>1: 
    cut_index = (count%len(flames) - 1) #-1 because indexing starts from 0 in computers
    if cut_index>=0:
        right = flames[cut_index+1:]
        left = flames[:cut_index]
        flames = right + left
    else: #Because when count = 6 then cut_index = -1 
        flames = flames[:len(flames)-1]
print(flames[0])

