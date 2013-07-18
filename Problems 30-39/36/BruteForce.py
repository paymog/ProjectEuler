'''
Created on 2013-01-22

@author: paymahn
'''

import CommonFunctions as cf

print str(bin(956978))

tally = 0
for i in range(1000000):
    if cf.is_palindrome(i) and cf.is_palindrome(str(bin(i))[2:]):
        tally += i
        print i
        
print tally