'''
Created on 2013-01-22

@author: paymahn
'''

'''
By Euclid we know:

a = m**2 - n**2
b = 2 * m * n
c = m**2 + n**2

for some m > n > 0 such that a < b

------

NOTE: 

if exactly one of m,n is even and gcd(m,n) = 1 then (a,b,c) is a primitive triplet

a = (m**2 - n**2 ) * d
b = 2 * m * n * d
c = (m**2 + n**2) * d

When d = 1, (a,b,c) are primitive

-----

The plan is to generate primitive triplets then find multpiles of each one until the sum
of a multiple is larger than 1000
'''
import CommonFunctions as cf
import time

t = time.time()

p = 1000
p_solutions = [0] * (p+1)
for n in range(1,p):    
    for m in range(n+1, p/2/n, 2): #increment by two to ensure that m%2 != n%2
        if cf.gcd(m, n) == 1:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            
            sum = a + b + c
            multiplier = 2
            while sum <= p:
                p_solutions[sum] += 1
                sum = a*multiplier + b*multiplier + c*multiplier
                multiplier += 1

max = max(p_solutions)
for i in range(len(p_solutions)):
    if p_solutions[i] == max: print i
    
print time.time() - t