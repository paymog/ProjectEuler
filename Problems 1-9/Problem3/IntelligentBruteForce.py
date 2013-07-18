'''
Created on Jan 17, 2013

@author: PaymahnMoghadasian
'''
number = 600851475143
factors = []

n = number
d = 2
while n > 1:
    while n % d == 0:
        if d not in factors:
            factors.append(d)
        n /= d
    
    d += 1
    
print factors[-1]
