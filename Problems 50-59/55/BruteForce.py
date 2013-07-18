'''
Created on 2013-01-25

@author: paymahn
'''

from CommonFunctions import is_palindrome

tally = 0

for i in range(1,10000):
    is_lychrel = True
    num = i
    for j in range(50):
        num = int(str(num)) + int(str(num)[::-1])
        if is_palindrome(num):
            is_lychrel = False
            break
    
    if is_lychrel:
        print i
        tally += 1
    
print tally