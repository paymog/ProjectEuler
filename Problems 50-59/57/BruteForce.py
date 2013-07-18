'''
Created on Jan 26, 2013

@author: PaymahnMoghadasian
'''
import CommonFunctions as cf
import math

def reduce(fraction):
    factor = cf.gcd(fraction[0], fraction[1])
    return (fraction[0]/factor, fraction[1]/factor)

def add(f1, f2):
    n1, d1 = f1
    n2, d2 = f2
    #print "%d / %d and %d / %d" %(n1,d1,n2,d2)
    
    n1,n2 = n1*d2, n2*d1
    d1 *= d2
    #print "%d / %d and %d / %d" %(n1,d1,n2,d2)
    
    return reduce((n1+n2, d1))

def divide(f1,f2):
    n1,d1 = f1
    n2,d2 = f2
    
    return reduce((n1*d2, n2*d1))

LIMIT = 1001
tally = 0
for i in range(1,LIMIT):
    term = (1,2)
    for j in range(1,i):
        term = divide((1,1), add((2,1), term))
    
    term = add((1,1), term)
    n, d = term
    
    if int(math.log10(n) + 1) > int(math.log10(d) + 1):
        tally += 1
        #print i, ',', term
        
print tally
    