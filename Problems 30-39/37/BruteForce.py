'''
Created on 2013-01-22

@author: paymahn
'''

'''
Can't find the 11th prime

'''
import CommonFunctions as cf
import time
import math

t = time.time()


primes = cf.generate_primes_less_than(1000000)

#remove primes that have even numbers
#turn into set for quick lookups
usable_primes = set([x for x in primes if not cf.contains_even_digit(x)])


tally = 0
count = 0
for x in usable_primes:
    if x > 7 and count < 11:
        
        
        #test left trucation
        left = True
        temp = x
        len = int(math.log10(temp)) + 1
        while len > 0 and left:
            temp %= 10**len
            if temp not in usable_primes:
                left = False
                
            len -= 1
        
        #test right truncation
        temp = x
        right = True
        while left and right and temp > 0:
            if temp not in usable_primes:
                right = False
            
            temp /= 10
                
        if left and right:
            print x
            count +=1
            tally += x


print count
print tally + 23 #23 was filtered out when we created the usable_primes set even though it is valid for this problem

print time.time() - t











