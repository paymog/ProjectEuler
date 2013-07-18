'''
Created on 2013-01-22

@author: paymahn
'''

'''
Turns out that 9 and 8 digit pandigital numbers are always divisible by 3

'''
import CommonFunctions as cf
import math

max = 7654322

primes = cf.generate_primes_less_than(max)

for i in reversed(primes):
    if cf.is_pandigital(i, int(math.log10(i)) + 1):
        print i
        break;