'''
Created on Jan 19, 2013

@author: PaymahnMoghadasian
'''

import operator

print sum(int(i) for i in str(reduce(operator.mul, [x for x in range(1, 101)])))

'''
from inside out:
enumerate all values from 1-100 (inclusive)
multiply all of those together with reduce(operator.mul, ...)
convert the product to a String
foreach character in the string, convert to an int
sum all of those ints
print the sum
'''
