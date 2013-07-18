'''
Created on 2013-01-23

@author: paymahn
'''
import CommonFunctions as cf
import time
t = time.time()

primes = cf.generate_primes_less_than(100000)
target_prime_factors = 4
target_consecutive = 4
consecutive = 0
result = 2*3*5*7

while consecutive < target_consecutive:
    result += 1
    
    if(len(cf.find_prime_factors(result, primes)) >= target_prime_factors):
        consecutive+= 1
    else:
        consecutive = 0
        
print "Done executing"
print time.time() - t
print result