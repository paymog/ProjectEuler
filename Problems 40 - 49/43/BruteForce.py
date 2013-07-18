'''
Created on 2013-01-22

@author: paymahn
'''

'''
fuck this, it's not working. I'm gonna try something different

'''
import CommonFunctions as cf
import itertools as it
import time

t = time.time()


pandigitals = [cf.tuple_to_num(x) for x in it.permutations(range(10))]
primes= cf.generate_primes_less_than(20)

tally = 0
for i in pandigitals:
    i = str(i)
    if len(i) == 10:
        valid = True
        for j in range(1,7):
            substr = i[j:j+3]
            prime = primes[j-1]
            if int(substr) % prime != 0:
                valid = False
                break
        
        if valid:
            tally += int(i)
          
print tally  
print time.time() -t