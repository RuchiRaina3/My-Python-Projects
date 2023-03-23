# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:22:17 2020

@author: lockd

                ROCK, PAPER AND SCISSOR GAME - CHEATING NOT ALLOWED
1. Both players will be asked to enter a 3-digit number
2. They will be asked to choose a position (i.e ones, tens, hundreds) of 
their specific number
3. The digit at the chosen position is mod by 3 and the result is compared  
with the digits assigned for ROCK, PAPER and SCISSOR for both the players.
4. Finally winner is declared as per the result of comparisons.             
"""

def game(p1,p2,num1,num2,pos1,pos2):
    
    po1 = int(num1[pos1])%3
    po2 = int(num2[pos2])%3
    
    if(p1_Assignments[po1] == p2_Assignments[po2]):
        print("Draw")
   
    elif(p1_Assignments[po1]=='ROCK' and p2_Assignments[po2]=='SCISSOR'):
        print(p1,' Won')
    elif(p1_Assignments[po1]=='SCISSOR' and p2_Assignments[po2]=='PAPER'):
        print(p1,' Won')
    elif(p1_Assignments[po1]=='PAPER' and p2_Assignments[po2]=='ROCK'):
        print(p1,' Won')
   
    elif(p1_Assignments[po1]=='SCISSOR' and p2_Assignments[po2]=='ROCK'):
        print(p2,' Won')
    elif(p1_Assignments[po1]=='PAPER' and p2_Assignments[po2]=='SCISSOR'):
        print(p2,' Won')
    elif(p1_Assignments[po1]=='ROCK' and p2_Assignments[po2]=='PAPER'):
        print(p2,' Won')

    

print("Welcome to the  ROCK, PAPER AND SCISSOR GAME - CHEATING NOT ALLOWED")

p1 = input("Name of Player1:  ")
p2 = input("Name of Player2:  ")

print()
print('To ensure that no one cheat, both of you will be asked to enter any 3-digit number.')
print('Then, you will select any position of your number i.e ones, tenths or hundreds.')
print()

p1_Assignments = {0:'PAPER', 1:'ROCK', 2:'SCISSOR'}
p2_Assignments = {0:'ROCK', 1:'SCISSOR', 2:'PAPER'}

while(1):
    
    
    print(p1,'Enter any 3-digit number:  ', end='')
    num1 = input()
    print(p2,'Enter any 3-digit number:  ', end='')
    num2 = input()
    
    pos1 = int(input('Player1, Enter the position:  '))
    pos2 = int(input('Player2, Enter the position:  '))
    
    game(p1,p2,num1,num2,pos1,pos2)
    
    choice = input('Do you want to continue? y/n:  ')
    if(choice=='n' or choice=='N'):
        print("Thanks For Playing")
        print("Have a Wonderful Day!!!")
        break
    
