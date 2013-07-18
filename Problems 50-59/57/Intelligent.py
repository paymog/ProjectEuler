'''
Created on Jan 26, 2013

@author: PaymahnMoghadasian
'''

'''
There's a pattern to the num and denom of the expanded fractions

The next num = 2*denom + num
The next denom = denom + num
'''
import math


num = 3
denom = 2
tally = 0
for i in range(1000):
    if int(math.log10(num)) > int(math.log10(denom)):
        tally += 1
        
    num, denom = 2*denom + num, denom + num
    
print tally