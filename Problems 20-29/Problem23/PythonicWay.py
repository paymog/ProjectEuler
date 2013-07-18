'''
Created on Jan 19, 2013

@author: PaymahnMoghadasian
'''
import CommonFunctions as cf

abundants = set(i for i in range(1, 28124) if sum(cf.find_divisors(i)) > i + i)

def abundantsum(i):
    return any(i - a in abundants for a in abundants)

print sum(i for i in range(1, 28124) if not abundantsum(i))
