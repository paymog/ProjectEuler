'''
Created on 2013-01-23

@author: paymahn
'''

'''
The nth pentagonal number is 1/3 of the 3n-1th triangular number
The mth hexagonal number is the 2m-1th triangular number

Every 2nd triangle number is hexagonal

The kth triangular number is (k+1)/2th hexagonal number (if (k+1) % 2 == 0)
The kth triangular number is (k+1)/3th pentagonal number (if (k+1)%3 == 0)

'''

import math

def is_pentagonal(num):
    return ((1 + math.sqrt(24*num + 1)) / 6).is_integer() and int(math.sqrt(24*num + 1)) % 6 == 5

i = 287

while True:
    n = i * (i+1) / 2
    if is_pentagonal(n):
        print n
        break
    i += 2 #every 2nd triangle number is hexagonal