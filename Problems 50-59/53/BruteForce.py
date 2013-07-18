'''
Created on 2013-01-24

@author: paymahn
'''
import math

nCr = lambda n,r: math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

tally = 0
for n in range(1,101):
    for r in range(1,n):
        if nCr(n,r) > 1000000:
            tally += 1
            
            
print tally