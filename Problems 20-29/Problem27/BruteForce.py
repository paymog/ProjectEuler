'''
Created on Jan 20, 2013

@author: PaymahnMoghadasian
'''
'''
Note that b must be prime and positive (I'm not sure if there's such a thing as a negative prime)

|a| must be bigger than b because primes can't be negative. If |a| < b and b is prime then f(1) is negative, which is not prime
EX: let f(n) = n*n + a*n + b
        f(1) = 1 + a + b
        If |a| < b then f(1) < 2


'''
import CommonFunctions as cf
import time

t = time.time()

values_of_b = cf.generate_primes_less_than(1000)
primes = set(cf.generate_n_primes(300))

best_a, best_b = None, None
best_n = 0

print time.time() - t
for b in values_of_b:
    for a in range(-b + 1, 10000):
        n = 0
        while n * n + a * n + b in primes:
            n += 1
        
        if n > best_n:
            best_n = n
            best_a = a
            best_b = b
            
print best_b * best_a
print time.time() - t
