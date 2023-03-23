# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:44:53 2020
@author: lockd

DOBBLE GAME: Spot the similarity
        There will be two sets of same number of symbols with only one symbol in common.
        Here, symbols are alphabets.
        The user has to spot the similar alphabet.
    
"""
import string
import random

#string.ascii_letters  Returns all lowercase and uppercase letters in the form of a string
#print(string.ascii_letters) 

def dobble():
    
    while(1):
        symbols = list(string.ascii_letters)    #Converts string into list

        set1 = [0]*5      #Initialises with 5 zeroes
        set2 = [0]*5  

        po1 = random.randrange(0,5)   #Any random number from 0 to 4 gets assigned to po which represents particular index where similar symbol is present
        po2 = random.randrange(0,5)   #po2 is for set 2

        similar = random.choice(symbols)    #A random alphabet from symbols get assigned to similar
        symbols.remove(similar)     #Removing that similar alphabet from list so that it doesn't get assigned to any other position

        if(po1 == po2):
            set1[po1] = similar
            set2[po2] = similar
        else:
            set1[po1] = similar
            set2[po2] = similar
    
        #Because in the upcoming loop, we are not going to assign po1 and po2
            set1[po2] = random.choice(symbols) 
            symbols.remove(set1[po2])
            set2[po1] = random.choice(symbols) 
            symbols.remove(set2[po1])

        i = 0    
        while(i<5):
            if(i!=po1 and i!=po2): 
                set1[i] = random.choice(symbols) 
                symbols.remove(set1[i])
                set2[i] = random.choice(symbols) 
                symbols.remove(set2[i])
            i = i+1
   
        print(set1)
        print(set2)

        ans = input("Which is the similar alphabet?  ")

        if(ans == similar):
           print("Right")
        else:
           print("Wrong")
     
        n = int(input("If you want to continue, press 1. Or, if you want to exit, press 0:  "))
    
        if(n==0):
            print("Thank You For Playing!!!")
            break
        
print("Welcome To the DOBBLE Game")
print("Let's Play")
print()
dobble()
    
    
