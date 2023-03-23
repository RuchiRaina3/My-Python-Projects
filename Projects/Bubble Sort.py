# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:04:33 2020

@author: lockd

                            BUBBLE SORT

"""

def Bubble_sort(l):   #Taking list as a parameter  
    
    n = len(l)
    
    for i in range(n):
        #range(0,3)=0,1,2
        for j in range(0, n-1-i):    #n-1 because if we have 3 elements in a list, then we will compare 1st element two times(with 2nd and 3rd number) and in the next iteration of i, the last element won't be compared
            if(l[j]>l[j+1]):
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
                
l = [66,23,2,12,9,0,56,5,98,3]
Bubble_sort(l)

for i in l:
    print(i)
            
    

