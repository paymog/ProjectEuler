'''
Created on Jan 19, 2013

@author: PaymahnMoghadasian
'''
tally = 0
a, b = 1, 1
term = 1
while len(str(a)) < 1000:
    if a % 2 == 0:
        tally += a
    
    a, b = b, a + b
    term += 1

print term
