# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:53:15 2020

@author: lockd

Fibonacci Sequence: 0, 1, 1, 2, 3, 5...
0th Fib. = 0
1st Fib. = 1

nth Fib. = n-1th Fib + n-2th Fib

"""
def fib(n): #n is position
#Base Case: which is obvious, don't need tp calculate
    if n<2:
        return n
    else:
        return (fib(n-1) + fib(n-2))

n = int(input('Enter the position whose fibonacci number you want to know: '))
if n<0:
    print('Fibonacci Numbers are not defined on negative numbers')
else:
    print('Fibonacci Number at position ',n,' is ',fib(n))
    





