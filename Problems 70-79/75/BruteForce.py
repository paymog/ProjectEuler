'''
Created on 2013-01-25

@author: paymahn
'''
import CommonFunctions as cf

p = 1500000
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
                
print len([x for x in p_solutions if x == 1])