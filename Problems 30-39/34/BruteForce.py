'''
Created on 2013-01-21

@author: paymahn
'''

'''
Upper bound of 7 digits --> 9!*7 = 2540160

'''

import math

MAX = math.factorial(9) * 7 + 1
factorials = [math.factorial(x) for x in range(10)]

tally = 0
for i in range(10,MAX):
    digit_sum = 0
    n=i
    while n > 0:
        digit_sum += factorials[n%10]
        n /= 10
        if digit_sum > i:
            break
        
    if digit_sum == i:
        print i
        tally += i
        
print tally