'''
Created on Jan 19, 2013

@author: PaymahnMoghadasian
'''
import CommonFunctions as cf

sum_of_divisors = {}
amicable_numbers = []
UPPER_BOUND = 10000

print cf.find_divisors(1)

for i in range(2, UPPER_BOUND):
    divisors = cf.find_divisors(i)
    divisors.remove(i)
    sum_of_divisors[i] = sum(divisors)

for i in sum_of_divisors:
    # print "Checking %d with sum %d" % (i, sum_of_divisors[i])
    if sum_of_divisors[i] != 1 and sum_of_divisors[i] < UPPER_BOUND and  i == sum_of_divisors[sum_of_divisors[i]] and i != sum_of_divisors[i]:
        if i not in amicable_numbers:
            amicable_numbers.append(i)
        
        if sum_of_divisors[i] not in amicable_numbers:
            amicable_numbers.append(sum_of_divisors[i])
        
print sum(amicable_numbers)
print amicable_numbers
print sum_of_divisors[6]
print sum_of_divisors[28]
