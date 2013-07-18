'''
Created on 2013-01-21

@author: paymahn
'''

'''
A 1-9 pandigital product is a 2-digit number
times a 3-digit number, or a 1-digit number
times a 4-digit number, with a product less
than 1e4.  (3 2 and 4 1 also works, but don't
give any extra products.)

'''
import CommonFunctions as cf

found_number = set()



for i in range(1,100):
    for j in range(100,10000):
         num_str = str(i) + str(j) + str(i*j)
         if len(num_str) == 9 and cf.is_pandigital(int(num_str), 9):
             found_number.add(i*j)
                
print sum(found_number)