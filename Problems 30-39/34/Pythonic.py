'''
Created on 2013-01-21

@author: paymahn
'''

import math

factorials = [math.factorial(x) for x in range(10)]
MAX = math.factorial(9)*7 + 1

print sum(x for x in range(10,MAX) if x == sum(factorials[int(y)] for y in str(x)))