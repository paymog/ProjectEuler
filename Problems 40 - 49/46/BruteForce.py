'''
Created on 2013-01-23

@author: paymahn
'''

import CommonFunctions as cf

MAX = 10000
primes = set(cf.generate_primes_less_than(MAX))
odd_composite = [x for x in range(1,MAX) if x%2==1 and x not in primes and x > 1]
squares = [x*x for x in range(1,MAX) if x*x <= MAX/2]

for i in odd_composite:
    goldbach = False
    for j in squares:
        if i - 2*j in primes and not goldbach:
            goldbach = True
            break
    
    if not goldbach:
        print i
        break

