'''
Created on Jan 27, 2013

@author: PaymahnMoghadasian
'''

import CommonFunctions as cf
import itertools as it

LOWER = 1000
UPPER = 9999

valid_nums = cf.generate_heptagonals(UPPER, lower=LOWER) + cf.generate_hexagonals(UPPER, lower=LOWER) + cf.generate_octagonals(UPPER, lower=LOWER) + \
cf.generate_pentagonals(UPPER, lower=LOWER) + cf.generate_squares(UPPER, lower=LOWER) + cf.generate_triangulars(UPPER, lower=LOWER)

valid_nums = set(x for x in valid_nums if '0' not in str(x))

t = [0] * 6
ordered_set = [0] * 6
for num in valid_nums:
      
    valid_triplet = []
    first_two = num / 100
    last_two = num % 100
    
    for x in valid_nums:
        if x % 100 == first_two:
            middle_num = last_two*100 + x / 100
            if middle_num in valid_nums:
                valid_triplet.append((num, middle_num, x))
    
    
    
        