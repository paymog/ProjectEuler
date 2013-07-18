'''
Created on 2013-01-23

@author: paymahn
'''

'''
this takes around 30 minutes, i think. It's awful

'''
import CommonFunctions as cf
from time import time


t = time()

LIMIT = 1000000
primes = cf.generate_primes_less_than(LIMIT)
prime_set = set(primes)

most_consecutive_primes = 0
best_prime = 2
for i in range(len(primes)):
    for k in range(i,len(primes)):
        sum += primes[k]
        if sum <= LIMIT and sum in prime_set and k-i + 1 > most_consecutive_primes:
            most_consecutive_primes = k-i+1
            best_prime = sum
   
print best_prime, ",", most_consecutive_primes