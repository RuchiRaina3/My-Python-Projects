1# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 21:44:06 2020

@author: lockd

                           MONTY HALL GAME
There are 3 doors, one contains BMW and other two contain goats.
There will be 10 rounds. Player will make choice of one door which contain BMW
Then he will be shown a door which contain goat and will be asked to make a swap.
We have to check the number of wins with swap and without swap.
"""
import random

doors = [0]*3      #List of Doors #Initialised to solve index error
goat_doors = [0]*2    #List of doors containing goats

swap = 0        #Wins with swap
dont_swap = 0   #Wins with don't swap

print('You have to choose a door among 0, 1 and 2')

j = 0
while(j<4):
   
    x = random.randint(0,2)     #Xth door contain BMW
    doors[x] = "BMW"
    
    for i in range(0,3):
        if(doors[i] == "BMW"):
            continue        #Move to next iteration without executing further code
        else:
            doors[i] == "Goat"
            goat_doors.append(i)
            
    choice = int(input("Your choice: ")) 
    
    open_door = random.choice(goat_doors)   #Opens one of the doors containing goat
    while(open_door == choice):             #Because that door shouldn't be opened which has chosen by the player
        open_door = random.choice(goat_doors)
    print("I am opening door ",open_door," for you. It contains a goat")   
    
    sw = input("Do you want to swap? y/n:  ")
    
    if(sw=='y' or sw=='Y'):
        if(doors[choice] == "BMW"):
            print('Player Loses')
        else:
            print('Player Wins')
            swap = swap + 1
    else:
        if(doors[choice] == "BMW"):
          print('Player Wins')
        else:
          print('Player Loses') 
          dont_swap = dont_swap + 1
          
    j = j+1   

print()
print('Total wins with swap = ',swap)
print('Total wins with dont_swap = ',dont_swap)           
        