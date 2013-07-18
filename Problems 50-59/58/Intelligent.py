'''
Created on 2013-01-25

@author: paymahn
'''
'''
Note: 1 has row=0 and column = 0. Row and column values increase by 1 as you go up or down (ie: the row above 1 is row 1
and the row below 1 is row 1)

n = row number

Numbers from middle to top left are of the form: (2*n)**2 + 1
Numbers from middle to top right are of the form (2*n)**2 - (2*n -1)
Numbers from middle to bottom left are of the form: (2*n)**2 + 2*n + 1
Numbers from middle to bottom right are of the form (2*n + 1)**2


The number of numbers on both diagonals = 4*n + 1
'''

import CommonFunctions as cf

#primes = cf.generate_primes_less_than(100000000)
#prime_set = set(primes)

num_primes = 0

for n in range(1,100000):
    tl = (2*n)**2 + 1
    tr = (2*n)**2 - (2*n -1)
    bl = (2*n)**2 + 2*n + 1
    num_nums = 4.0*n + 1
    #br = (2*n + 1)**2 #this will never be prime
    
    
    if cf.Miller_Rabin_primality_test(tl):
        num_primes += 1
    if cf.Miller_Rabin_primality_test(tr):
        num_primes += 1
    if cf.Miller_Rabin_primality_test(bl):
        num_primes += 1
        
    if num_primes / num_nums <= 0.1:
        print n*2 + 1
        print bl
        break