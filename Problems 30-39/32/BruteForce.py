'''
Created on 2013-01-21

@author: paymahn
'''
from httplib import FOUND

found_number = set()


def has_repeated_digits(num):
    x = str(num)
    return len(set(x)) == len(x)

def is_pandigital(num, n):
    digits = [0] * n
    for i in range(len(str(num))):
        digit = (num / 10**i) % 10
        if digit < 1 or digit > n:
            return False
        
        digits[digit-1] += 1
        if digits[digit-1] > 1:
            return False
        
    for i in digits:
        if i != 1:
            return False
        
    return True

tally = 0
for i in range(1,9876):
    if not has_repeated_digits(i):
        for j in range(i, 9876):
            num_str = str(i) + str(j) + str(i*j)
            if len(num_str) == 9 and is_pandigital(int(num_str), 9):
                found_number.add(i*j)
                
                

        
print sum(found_number)