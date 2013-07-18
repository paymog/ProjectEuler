'''
Created on Jan 17, 2013

@author: PaymahnMoghadasian
'''

'''
Just need to minimize prime factors.
To expand, we need to cover all possible numbers 2,3,4,5,...,20

Note that 4 = 2*2, 16 = 2^4, 18 = 2*3*3
Also note that all primes from 1 to 20 must be included.

Therefore

answer = 2*3*5*7*11*13*17*19 --> this covers all the primes. We're still missing factors such as 4
We can add 4 by throwing in another *2
We have 6 (2*3)
We need 8,9,16

therefore

answer = 2^4*3^2*5*7*11*13*17*19
'''
