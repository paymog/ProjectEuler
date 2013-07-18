'''
Created on 2013-01-29

@author: paymahn
'''

'''
Use Eulers totient function:
http://www.math.okstate.edu/~wrightd/crypt/lecnotes/node18.html
'''
import CommonFunctions as cf

MAX = 10**6
totient = [0]*(MAX+1)
primes = cf.sieve_of_Erastothenes(MAX)
for i in range(2,MAX+1):
    factors = cf.find_prime_factors(i, primes)
    product = 1
    for factor in factors:
        product *= factor**factors[factor] - factor**(factors[factor]-1)
        
    totient[i] = product
    
print sum(totient) * 3/7
