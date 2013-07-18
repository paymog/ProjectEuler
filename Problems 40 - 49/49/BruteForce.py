'''
Created on 2013-01-23

@author: paymahn
'''
import CommonFunctions as cf
import itertools as it
import time

t = time.time()


primes = cf.generate_primes_less_than(10000) #generate primes less than 10000
primes = set(x for x in primes if x > 1000) #remove primes less than 1000 (we only have 4 digit primes now)

for i in primes:
    permutations = [cf.tuple_to_num(x) for x in it.permutations(str(i))] #get all the permutations of the digits of the current prime
    permutations = set(x for x in permutations if x in primes) #remove duplicate permutations and non prime permutations
    triplets = [x for x in it.permutations(permutations, 3)] #it's hard to explain this one succintly, use a debugger
    for x in triplets: #test each triplet and print the triplet if it's valid
        sorted_triplet = sorted(x)
        if sorted_triplet[2] - sorted_triplet[1] == sorted_triplet[1] - sorted_triplet[0]:
            print sorted_triplet
    
    
print time.time() - t