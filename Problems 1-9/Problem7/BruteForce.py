'''
Created on Jan 17, 2013

@author: PaymahnMoghadasian
'''


def is_prime(num):
    root = num ** 0.5
    
    for i in primes:
        if num % i == 0:
            return False
        if i > root:
            return True
        
    return True

primes = [2]


next_num = 3
while len(primes) < 10001:
    if(is_prime(next_num)):
        primes.append(next_num)
        
    next_num += 1
    
    
print primes[-1]
