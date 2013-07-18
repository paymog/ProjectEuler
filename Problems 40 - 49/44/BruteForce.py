'''
Created on 2013-01-23

@author: paymahn
'''

'''
Pi - P(i-1) = P(i-1) - P(i-2) + 3

I can't reason what an upper bound might be. Let's brute force and hope.

'''
import CommonFunctions as cf
import time
import math

t = time.time()

pentagonals = cf.generate_n_pentagonals(2500)

print time.time() - t

pentagonals_set = set(pentagonals)

print time.time() - t
 
best_difference = 1000000000

for k in range(1,len(pentagonals)):
    for j in reversed(range(0, k)):
        sum = pentagonals[j] + pentagonals[k]
        difference = pentagonals[k] - pentagonals[j] 
        if sum in pentagonals_set and difference in pentagonals_set and difference < best_difference:
            best_difference = difference
            break
            
print best_difference
print time.time() - t