'''
Created on 2013-01-24

@author: paymahn
'''
import CommonFunctions as cf

from time import time

t = time()

LIMIT = 100000000
primes = cf.generate_primes_less_than(LIMIT/2)
prime_set = set(primes)

tally = 0
i = 0
while tally <= LIMIT:
    tally += primes[i]
    i += 1
    
i -= 1
tally -= primes[i]


i = 0
while tally not in prime_set:
    tally -= primes[i]
    i += 1
print tally


print time() - t