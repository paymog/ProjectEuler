'''
Created on 2013-01-22

@author: paymahn
'''
import CommonFunctions as cf


'''
When n = 2, we can only test numbers between 5000 and 9999 (inclusive). The concatenated product of
anything outside of this range with (1,2) will not produce a 9 digit number.

When n = 3, we have an upper test bound of 333. 334*1 = 334, 334*2 = 668,334*3 = 1002 -->3346681002 has more than 9 digits
We also have a lower bound of 100

When n = 4, we have an upper test bound of 100, probably

'''

import time
t = time.time()

largest = 0
for n in range(2,10):
    upper_bound = 10000 #exclusive
    lower_bound = 1
    
    if n == 2:
        lower_bound = 5000
    elif n == 3:
        upper_bound = 334
        lower_bound = 100
    else:
        upper_bound = 100
        
    for i in range(lower_bound, upper_bound):
        num = ''
        for x in range(1,n+1):
            num += str(i*x)
            
        num = int(num)
        if num > largest and cf.is_pandigital(num, 9):
            largest = num
            
print largest

print time.time() - t 