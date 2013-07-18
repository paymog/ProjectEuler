'''
Created on 2013-01-21

@author: paymahn
'''
import CommonFunctions as cf
import math

primes = set(cf.generate_primes_less_than(1000000))
count = 0
for i in primes:
    #print "Testing prime", i
    len = int(math.log10(i) + 1)
    temp = i
    valid = True
    for j in range(len):
        temp = (temp % 10**(len-1)) * 10 + temp/10**(len-1)
        if temp not in primes:
            valid = False
            break
    
    if valid:
        print i
        count += 1
        
print count