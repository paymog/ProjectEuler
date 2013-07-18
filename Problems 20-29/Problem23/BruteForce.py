'''
Created on Jan 19, 2013

@author: PaymahnMoghadasian
'''
import CommonFunctions as cf

UPPER_BOUND = 28123  # inclusive

abundant_numbers = []

for i in range(2, UPPER_BOUND + 1):
    divisors = cf.find_divisors(i)
    divisors.remove(i)
    sum_of_divisors = sum(divisors)
    
    if sum_of_divisors > i:
        abundant_numbers.append(i)
        
tally = 0
abundant_numbers.sort()
print len(abundant_numbers)

for i in range(1, UPPER_BOUND + 1):
    if i % 1000 == 0: 
        print "At %d with tally %d" % (i, tally)
    for j in abundant_numbers:
        if j > i / 2:
            tally += i
            break
        
        if cf.binary_search(abundant_numbers, i - j) != -1:
            break
            
            
print tally
