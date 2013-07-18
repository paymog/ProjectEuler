'''
Created on 2013-01-28

@author: paymahn

The idea is to make a sieve and cross of multiples.
All unique fractions are kept unmarked.
'''
import CommonFunctions as cf
from time import time

t = time()

MAX = 50


primes = set(cf.sieve_of_Erastothenes(MAX))
tally = 0
for denom in range(2,MAX + 1):
    if denom in primes:
        tally += denom - 1
    else:
        if denom %2 == 0:
            jump = 2
        else:
            jump = 1
        
        for num in range(1,denom,jump):
            if cf.gcd(num, denom) == 1:
                tally += 1


print '(%d,%d),'%(MAX, tally)
    
print time()- t