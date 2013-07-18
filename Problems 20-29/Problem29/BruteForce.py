'''
Created on Jan 21, 2013

@author: PaymahnMoghadasian
'''
import time

t = time.time()

powers = set()

for a in range(2, 101):
    for b in range(2, 101):
        powers.add(a ** b)
        
# powers = set(powers)
print len(powers)

print time.time() - t
