# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:47:57 2020

@author: lockd

Spiral Traversing Colourful
"""

import turtle
import random

t = turtle.Turtle()

dot_distance = 25 #Distance

t.penup()
t.setpos(-250, 250)
t.pendown()
t.speed(7)

colours_list = ['orange','blue','red','green','violet','black','brown','pink','yellow','grey']


def spiral(r, c):
    k = 0  #Index of staring row 
    l = 0  #Index of staring column  
    
    while(k<r and l<c):
        
        #Printing 1st row from remaining rows.
        for i in range(l, c):
            col = random.choice(colours_list)
            t.color(col)
            t.forward(dot_distance)
           
        k+=1
        
        t.right(90)
        #Printing last column from remaining columns.
        for i in range(k, r):
            col = random.choice(colours_list)
            t.color(col)
            t.forward(dot_distance)
             
        c-=1
        t.right(90)
        
        
        #Printing last row from remaining rows.
        for i in range(c-1, l-1, -1):
            col = random.choice(colours_list)
            t.color(col)
            t.forward(dot_distance)
        
        r-=1
        t.right(90)
        
        #Printing 1st column from remaining columns.
        for i in range(r-1, k-1, -1):
            col = random.choice(colours_list)
            t.color(col)
            t.forward(dot_distance)
        
        l+=1
        t.right(90)
        

spiral(20, 20)
turtle.done()



