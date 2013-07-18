'''
Created on 2013-01-22

@author: paymahn
'''

import itertools as it
import CommonFunctions as cf

pan9 = [int(''.join(map(str,x))) for x in it.permutations(range(1,8),7)]
pan9.sort(reverse=True)

primes = cf.generate_primes_less_than(int(7654321**0.5))

for i in pan9:
    if cf.is_prime(i, primes):
        print i
        break
    
print "finished"