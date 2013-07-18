'''
Created on 2013-01-24

@author: paymahn
'''

def digit_count(num):
    result = [0] * 10
    while num > 0:
        result[num%10] += 1
        num /= 10
        
    return result


for i in range(100000, int(1000000/6) + 1):
    if digit_count(i) == digit_count(i*2) == digit_count(i*3) == digit_count(i*4) == digit_count(i*5) == digit_count(i*6):
        print digit_count(i)
        print i