'''
Created on 2013-01-23

@author: paymahn
'''

'''
This shit doesn't work. Fuck it.

'''

import CommonFunctions as cf

LIMIT = 100
primes = cf.generate_primes_less_than(LIMIT)
cache = [0] * (LIMIT + 1) 

def sum_of_primes(n, last_index_subtracted):
    if n < 0 or n == 1 or n < primes[last_index_subtracted + 1]:
        return 0
    
    if cache[n] > 0 and n > primes[last_index_subtracted]:
        return cache[n] + 1
    
    if n == 0:
        return 1
    
    if last_index_subtracted == -1:
        longest = 0
        last_index_subtracted += 1
        while last_index_subtracted < len(primes) and primes[last_index_subtracted] <= n:
            length = sum_of_primes(n - primes[last_index_subtracted], last_index_subtracted)
            longest = max(longest, length)
            last_index_subtracted += 1
            
        cache[n] = longest
    else:
        last_index_subtracted += 1
        cache[n] = sum_of_primes(n - primes[last_index_subtracted], last_index_subtracted) 
    
    
    return cache[n]

for i in primes:
    sum_of_primes(i, -1)
    
for i in range(len(cache)):
    print i, 'can be written as the sum of', cache[i], 'consecutive primes'