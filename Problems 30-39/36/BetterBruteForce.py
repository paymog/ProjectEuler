'''
Created on 2013-01-22

@author: paymahn
'''

import CommonFunctions as cf

'''
A palindromic number < 1000000 is of the form

a*100000 + b*10000 + c*1000 + c*100 * b*10 + a
=
a*100001 + b*10010 + c*1100

'''

import time

t = time.time()

tally = 0
for a in range(1,10,2):
    num1 = a
    num2 = a*11
    
    if cf.is_palindrome(str(bin(num1))[2:]):
        tally += num1
    if cf.is_palindrome(str(bin(num2))[2:]):
        tally += num2
        
    for b in range(10):
        num3 = a*101 + b*10
        num4 = a*1001 + b*110
        
        if cf.is_palindrome(str(bin(num3))[2:]):
            tally += num3
        if cf.is_palindrome(str(bin(num4))[2:]):
            tally += num4
            
        for c in range(10):
            num5 = a*10001 +  b*1010  + c*100
            num6 = a*100001 + b*10010 + c*1100
            
            if cf.is_palindrome(str(bin(num5))[2:]):
                tally += num5
            if cf.is_palindrome(str(bin(num6))[2:]):
                tally += num6
            '''
            #The following is for fun to see what happens if we test all numbers up to 10 digits longs. Still takes under
            #0.5sec
            for d in range(10):
                num7 = a*1000001 +  b*100010  + c*10100 + d*1000
                num8 = a*10000001 + b*1000010 + c*100100 + d*11000
                
                if cf.is_palindrome(str(bin(num7))[2:]):
                    tally += num7
                if cf.is_palindrome(str(bin(num8))[2:]):
                    tally += num8
                    
                for e in range(10):
                    num9 = a*10**8 +  b*10**7  + c*10**6 + d*10**5 + e*10**4 + d*10**3 + c*10**2 + b*10 + a
                    num10 = a*10**9 +  b*10**8  + c*10**7 + d*10**6 + e*10**5 + e*10**4 + d*10**3 + c*10**2 + b*10 + a
                    
                    if cf.is_palindrome(str(bin(num9))[2:]):
                        tally += num9
                    if cf.is_palindrome(str(bin(num10))[2:]):
                        tally += num10
                '''
print tally

print time.time() - t