
# Fibonnaci

import random
import os
import sys

# from time import sleep
# Fibonacci numbers

# a = b = 1
# counter = 0
# num_digits = int(input('How many digits will you want to go? '))
# input 9 result is 1	2	3	5	8	13	21	34	55
#
# while counter < num_digits:
#
#     print(b, end="\t")
#     ''' Add the a + b first then old "b" goes to "a" then new "b" = a + b
#         Like c = a + b, a = b, print c (= new b), then new b plus a.'''
#     a, b = b, a+b
#     #Like counter = (counter + 1)
#     counter+= 1

# '''---------------------------------------------------------------'''
# #Use the while condition
# end_line =8
# #Initialize two numbers
# a, b = 0, 1
# n = 0
#
# #Program!
# while n <= end_line:
#     print(a,end = ' ')
#     #sleep(1)
#     a, b = b, a+b
#     n += 1
#
# print('\n')# 0 1 1 2 3 5 8 13 21
# '''-----------------------------------------------------------------'''
#Use the range condition

# def fib(n):
#     a, b = 0, 1
#
#     for i in range(n+1):
#         print(a, end=' ')
#         a, b = b, a+b
#
# fib(9) #0 1 1 2 3 5 8 13 21 34
# '''-------------------------------------------------------------------'''
## ''' Optimize code by ex. fib(n-1) + fib(n-2)'''
def fib(n):
# Program
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        a = fib(n-1)+fib(n-2)
        print(f'{fib(n-1)}  {fib(n-2)}  {a}')
        return fib(n-1)+fib(n-2)
#
print(fib(5))#34
#
# def fib_1(n):
#     # Program
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     else:
#         result=(n-1)+(n-2)
#
#         print(a)
#         fib_1(n-1)+fib_1(n-2)
#
# fib_1(9)
import functools
# from functools import lru_cache

@functools.lru_cache(maxsize=500)
def fib_fnc(n):

  #Check that the input is a positive integer
  if type(n) != int:
    raise TypeError('n must be a positive integer')

  if n < 0:
    raise ValueError('n must be a positive integer')

  # Compute the nth term
  if n == 0 or n == 1:
    return 1
  else:
    return fib_fnc(n-1) + fib_fnc(n-2)

# print(fib_fnc(50))

#Convert to ratio. Goes to the golden ratio 1.618033988xxxxxx
# for x in range(1, 51):
#   print(fib_fnc(x+1) / fib_fnc(x))



