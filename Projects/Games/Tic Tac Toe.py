# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:44:08 2020

@author: lockd


                TIC TAC TOE
"""

import numpy  

board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])

p1s = 'X'
p2s = 'O'

def check_rows(symbol):
    count = 0
    for r in range(3):
        for c in range(3):
            if board[r][c]==symbol:
                count = count+1
            else:
                break
        if count==3:
            print(numpy.matrix(board))
            print(symbol,'Won')
            return True
    return False

def check_cols(symbol):
    count = 0
    for c in range(3):
        for r in range(3):
            if board[r][c]==symbol:
                count = count+1
            else:
                break
        if count==3:
            print(numpy.matrix(board))
            print(symbol,'Won')
            return True
    return False

def check_diagonals(symbol):
    if board[0][0]==symbol and board[1][1]==symbol and board[2][2]==symbol:
        print(numpy.matrix(board))
        print(symbol,'Won')
        return True
    if board[0][2]==symbol and board[1][1]==symbol and board[2][0]==symbol:
        print(numpy.matrix(board))
        print(symbol,'Won')
        return True
    return False
    
def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)    


def place(symbol):  #Place where the player wants to place his symbol
    print(numpy.matrix(board))
    while(1):
        row = int(input('Enter Row- 1, 2 or 3: '))
        col = int(input('Enter Column- 1, 2 or 3: '))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print('Invalid input. Please try again')
    board[row-1][col-1] = symbol
    

def play():
    for i in range(9):
        if(i%2 == 0):
            print('X turn')
            place(p1s)
            if won(p1s):
                break
         
        else:
            print()
            print('O turn')
            place(p2s)
            if won(p2s):
                break
         
    if not(won(p1s)) and not(won(p2s)):
        print('DRAW')
        
play()
        
        

