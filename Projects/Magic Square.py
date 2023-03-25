# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:47:42 2020

Magic Square

Mostly possible when n is odd (n is the size of square i.e. no. of rows and no. of columns)
For magic square of 3, the numbers which have to be filled are 1 to 9
Sum of each row,each column and each diagnol is: n(n^2+1)/2

Steps:
    1. Position of 1 is (n/2,n-1) = (r,c) where r is row and c is column
    2. Position of next number is (r-1,c+1). If after calculation: r=-1, then 
    make r=n-1 and if c=n, then c=0
    3. Find position of successive numbers by the same formula.
    4. If counted position has already occupied, make r=r+1 and c=c-2. If after
    calculation: r=-1 and also if c=n, then switch it to (0,n-2)
      
"""

def Magic_Square(n):        #Function to find magic square of size n
    
    magicSq=[]          
    for r in range(n):       #To initialize magicSq with 0
        l = []
        for c in range(n):
            l.append(0)
        magicSq.append(l)

#Directly initializing magicSq with 0
#magicSq=[[0 for i in range(3)] for j in range(3)] 
    
    
    num = n*n       #Total numbers to be filled in magicSq
    count = 1       #For counting numbers till n*n
    r = n//2        #Row position
    c = n-1         #Column position
    
    while(count<=num):
        
        if(r==-1 and c==n):     #Condition 5
            r=0
            c=n-2
        else:                   #Condition 2
            if(r<0):            
                r=n-1
            if(c==n):
                c=0
        
        if(magicSq[r][c]!=0):
            r = r+1
            c = c-2
            continue            #Next satements won't get executed and control goes to while() and count has not incremented yet
        
        else:           
            magicSq[r][c] = count
            count=count+1
       
        r = r-1                 #Condition 2
        c = c+1
           
    
    for r in range(n):         #To print magicSq in matrix form
        for c in range(n):
            print(magicSq[r][c], end=' ')
        print()
    print()
    print("The sum of each row/column/diagonal is: ", n*(n*n+1)/2)
        
num = input("Write the number whose magic square you want to find (Remember this is odd order Magic square): ")
num = int(num)
print()

Magic_Square(num)


