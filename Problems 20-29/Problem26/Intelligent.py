'''
Created on Jan 20, 2013

@author: PaymahnMoghadasian
'''

'''
This solution uses multiplicative orders to find the correct answer

We're looking for Full Reptend Primes:
    http://mathworld.wolfram.com/FullReptendPrime.html
    
    We're looking for p < 1000 such that k=p-1 for 10**k % p == 1
    10**k % p == 1 is realted to the multiplicative order. See below


http://en.wikipedia.org/wiki/Multiplicative_order


I think that if we find the largest reptend prime < 1000, it will be our answer
'''

import CommonFunctions as cf
import time

t = time.time()

print cf.generate_reptend_primes_less_than(1000)[-1]

        
print time.time() - t
