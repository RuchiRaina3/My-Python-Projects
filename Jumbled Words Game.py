# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 20:07:19 2020

JUMBLED WORDS GAME
There are two players.
For each player's turn computer gives a jumpled word to player and the
player has to guess it. For each correct answer, the player gets a point.
The player with higher points wins.
"""


import random      #To use random function

def choose():   #Returns any random word from list words
    words = ['Laptop','Water','Apple','World','Earth','Father','Mother','Light']
    pick = random.choice(words) #A random word from words is assigned to pick
    return pick

def jumble(word):   #For jumbling
    jumbled = "".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,po1,po2):
    print(p1n,"with score: ",po1)
    print(p2n,"with score: ",po2)
    if(po1>po2):
        print(p1n,",is the winner")
    else:
        if(po1<po2):
            print(p2n,",is the winner")  
        else:
            print("Draw")
        

def play():  #Function for game
    print("Welcome to the JUMBLED WORDS GAME")
    
    p1 = input("Player 1: Enter your name ")
    p2 = input("Player 2: Enter your name ")
    print()
    
    points1 = 0
    points2 = 0
    
    turn = 1        #For odd no. P1 turn and for even nu. P2 turn
    
    while(3):       #To make while loop run, any constant except 0 can be used
        pickedWord = choose()       #PickedWord is var. and choose is a fun.
        qn = jumble(pickedWord)      #For jumblig oicked word
        print(qn)
         
        if(turn%2!=0):              #P1 turn
            print(p1,"Your turn")
            ans = input("What's on your mind ")
            
            if(ans==pickedWord):
                points1 = points1 + 1
                print("Right Answer. Your score is: ",points1)
            else:
                print("Ohho! Wrong answer. I thought: ",pickedWord)
                print("Better luck next time!!! Your score is: ",points1)
          
            c = input("Press 1 to continue and 0 to quit: ")
            print()
            c = int(c)
            
            if(c==0):
                thank(p1,p2,points1,points2)
                break;
                
        # P2
        else:
           print(p2,"Your turn")
           ans = input("What's on your mind ")
           
           if(ans==pickedWord):
                points2 = points2 + 1
                print("Right Answer. Your score is: ",points2)
           else:
                print("Ohho! Wrong answer. I thought: ",pickedWord)
                print("Better luck next time!!! Your score is: ",points2)
          
           c = input("Press 1 to continue and 0 to quit ")
           c = int(c)
           
           if(c==0):
                break;
                
        turn = turn + 1
        
play()          
            
            