'''
Created on 2013-01-28

@author: paymahn
'''

import itertools as it
import CommonFunctions as cf


def is_concat_prime(num1, num2):
    concat1 = int(str(num1) + str(num2))
    concat2 = int(str(num2) + str(num1))
    #return (cf.Miller_Rabin_primality_test(concat1) and cf.Miller_Rabin_primality_test(concat2))
    return concat1 in prime_set and concat2 in prime_set

#Following three lines are ugly as fuck. Basically, read in a file containing prime numbers
#and store them into various lists
prime_string = open('primes.txt').read()
primes = [int(x) for x in prime_string.split(',')][1:1300]
prime_set = set(int(x) for x in prime_string.split(','))

open('primes.txt', 'w').write(','.join(map(str,primes)))

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        
        if is_concat_prime(primes[i], primes[j]):
            for k in range(j+1, len(primes)):
                
                if is_concat_prime(primes[i], primes[k]) and is_concat_prime(primes[j], primes[k]):
                    for m in range(k + 1, len(primes)):
                        
                        if is_concat_prime(primes[i], primes[m]) and is_concat_prime(primes[j], primes[m]) and \
                        is_concat_prime(primes[k], primes[m]):
                            for p in range(m+1, len(primes)):
                                
                                if is_concat_prime(primes[i], primes[p]) and is_concat_prime(primes[j], primes[p]) and \
                                is_concat_prime(primes[k], primes[p]) and is_concat_prime(primes[m], primes[p]):
                                    print "%d,%d,%d,%d,%d" % (primes[i],primes[j],primes[k],primes[m],primes[p])
                                    print "sum =", primes[i]+primes[j]+primes[k]+primes[m]+primes[p]