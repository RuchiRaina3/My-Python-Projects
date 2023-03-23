# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:11:36 2020

@author: lockd

Guess The Movie

"""
import random

movies = ['dhammal','dangal','anand','yaadon ki baaraat','karz','blood diamond','jojo rabbit','intelligent khiladi','dangerous khiladi','lucky the racer ','shivaji the boss','war','haathi mere saathi','gadar','ghayal']

def create_qn(movie):
    temp = []
    for i in range(len(movie)):
        if(movie[i]==' '):
            temp.append(" ")
        else:
            temp.append('*')
    qn = ''.join(str(x) for x in temp) #Convert each x in temp into string and join it
    return qn

def letter_is_present(letter, movie):
    c = movie.count(letter) #Count can also be used for string
    if(c==0):
        return False
    else:
        return True
    
def unlock(qn,letter,movie): #To modify question
    modified_qn = []
    
    for i in range(len(movie)):
        if(movie[i]==' ' or movie[i]==letter):
            modified_qn.append(movie[i])
        else:
            if(qn[i]=='*'):
                modified_qn.append(qn[i])  #If that position has not guessed yet
            else:
                modified_qn.append(qn[i])  #If that position has guessed
    modified_qn = ''.join(str(x) for x in modified_qn)
    return modified_qn           
    
def play():
    
    print("WELCOME TO GUESS THE MOVIE")
    
    p1 = input("Player1 Enter your name:  ")
    p2 = input("Player2 Enter your name:  ")
    
    pp1 = 0         #Player1 points
    pp2 = 0         #Player2 points
    
    turn = 1
    
    willing = True  #Player's choice to play the game
    
    while(willing):
        
        if(turn%2 == 1):    #Player1's turn
            print()
            print(p1," your turn")
            picked_movie = random.choice(movies)
            qn = create_qn(picked_movie)
            modified_qn = qn    #Need later
            print()
            print(qn)   
            
           
            not_said = True
            while (not_said):
                letter = input("Your letter:  ")
                if(letter_is_present(letter,picked_movie)):
                    print(letter," is found")
                    modified_qn = unlock(modified_qn,letter,picked_movie)
                    print(modified_qn)
                    g = int(input("Press 1 to guess the movie or 2 to unlock another letter:  "))
                    if(g==1):
                        ans = input("Your guess:  ")
                        if(ans==picked_movie):
                            print('Correct')
                            pp1 = pp1 + 1
                            print(p1,'Your score: ',pp1)
                            not_said = False
                        else:
                            print("Wrong Answer. Try again")
                else:
                    print(letter,' not found')
                    c = int(input("Press 1 to continue or 0 to quit:  "))
                    if(c==0):
                        print()
                        print("Movie is: ",picked_movie)
                        print(p1," Your score: ",pp1)
                        
                        not_said = False
                        
        else:   #Player2's turn
            print()
            print(p2," your turn")
            picked_movie = random.choice(movies)
            qn = create_qn(picked_movie)
            modified_qn = qn    #Need later
            print()
            print(qn)
            
            not_said = True
            while (not_said):
                letter = input("Your letter:  ")
                if(letter_is_present(letter,picked_movie)):
                    print(letter," is found")
                    modified_qn = unlock(modified_qn,letter,picked_movie)
                    print(modified_qn)
                    g = int(input("Press 1 to guess the movie or 2 to unlock another letter:  "))
                    if(g==1):
                        ans = input("Your guess:  ")
                        if(ans==picked_movie):
                            print('Correct')
                            pp2 = pp2 + 1
                            print(p2,'Your score: ',pp2)
                            not_said = False
                        else:
                            print("Wrong Answer. Try again")
                else:
                    print(letter,' not found')
                    c = int(input("Press 1 to continue or 0 to quit:  "))
                    if(c==0):
                        print()
                        print("Movie is: ",picked_movie)
                        print(p2," Your score: ",pp2)
                        not_said = False
                       
        
        turn = turn + 1  
        p = int(input("Press 1 to continue with the game or 0 to exit the game:  "))
        if(p==0):
            print()
            print(p1," Your score: ",pp1)
            print(p2," Your score: ",pp2)
            print("Thanks for Playing")
            print("Have a nice day")
            willing = False
            
play()             