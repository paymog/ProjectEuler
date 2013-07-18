'''
Created on Jan 18, 2013

@author: PaymahnMoghadasian
'''

# this was made better by implement the sieve of Erastothene in CommonFunctions.py

import CommonFunctions as cf

print sum(cf.generate_primes_less_than(2000000))
