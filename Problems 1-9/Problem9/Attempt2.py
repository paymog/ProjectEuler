'''
Created on Jan 18, 2013

@author: PaymahnMoghadasian
'''

'''
We know:

a**2 + b**2 = c**2
a + b + c = 1000

Just need a third equation to solve this in constant time

---------

a**2 + b**2 = (1000 - a - b) ** 2
a**2 + b**2 = 1000000 - 2000a - 2000b + a**2 + 2*ab + b**2
2000a + 2000b = 1000000 + 2*ab

--------

New idea, we can assume that b will always be bigger than a to solve faster

Can also assume a < b < c  <---- turns out this doesn't help me
'''

'''
I couldn't think of a third equation, however, this is SIGNIFICANTLY faster than my previous attempt
'''

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        # if 2000 * a + 2000 * b == 1000000 + 2 * a * b: #it's easier to just clean this up
        if a * a + b * b == (1000 - a - b) ** 2:
            print a * b * (1000 - a - b)
