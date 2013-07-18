'''
Created on 2013-01-24

@author: paymahn
'''
import CommonFunctions as cf 
from time import time
import itertools as it
import math

def replace(num, digit, locations):
    result = num
    for i in locations:
        result -= num % 10**(i+1)
        result += digit*10**i
        result += num % 10**i
            
    return result


t = time()


LIMIT = 1000000
primes = cf.generate_primes_less_than(LIMIT)
prime_set = set(primes)
valid_primes = [x for x in primes if x > 100109]


for p in primes:
    length = int(math.log10(p)) + 1
    for x in it.combinations(range(length),3): #not sure why the 3 works, but it does
        primes_created = []
        for r in range(10):
            new_num = replace(p,r,x) #replaces digits indicated by x with the digit r in the number p
            
            if new_num > 0 and int(math.log10(new_num)) + 1 == length and new_num in prime_set:
                primes_created.append(new_num)
        
        if len(primes_created) == 8 and p in primes_created:
            print p, x, primes_created
            print time() - t
            exit()


