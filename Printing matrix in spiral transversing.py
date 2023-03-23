# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:42:31 2020

@author: lockd

Printing Matrix In Spiral Traversing form

"""


def spiral(r, c, a):
    k = 0  #Index of staring row 
    l = 0  #Index of staring column
    
    while(k<r and l<c):
        
        #Printing 1st row from remaining rows.
        for i in range(l, c):
            print(a[k][i], end=' ')
            
        k+=1
        
        #Printing last column from remaining columns.
        for i in range(k, r):
            print(a[i][c-1], end=' ')
            
        c-=1
        
        #Printing last row from remaining rows.
        for i in range(c-1, l-1, -1):
            print(a[r-1][i], end=' ')
        r-=1
            
        #Printing 1st column from remaining columns.
        for i in range(r-1, k-1, -1):
            print(a[i][l], end=' ')
        l+=1


#Initializing the matrix in the form of a list
a = []
s = int(input("Enter the size of matrix: "))
count = 1
for i in range(s):
    l = []
    for j in range(s):
        l.append(count)
        count+=1
    a.append(l)
    
spiral(s, s, a)

