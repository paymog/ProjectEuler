'''
Created on 2013-01-25

@author: paymahn
'''

import math

cache = [math.factorial(x) for x in range(0,101)]


tally = 0
for n in range(1,101):
    for r in range(1,n):
        if cache[n]/(cache[r]*cache[n-r]) > 1000000:
            tally += 1
            
            
print tally