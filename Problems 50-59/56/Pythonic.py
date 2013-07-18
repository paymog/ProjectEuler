'''
Created on 2013-01-25

@author: paymahn
'''

MAX = 99

def digital_sum(n):
    result = 0
    
    while n > 0:
        result += n % 10
        n /= 10
    
    return result


print max([digital_sum(a**b) for a in range(1,MAX +1) for b in range(1,MAX+1)])