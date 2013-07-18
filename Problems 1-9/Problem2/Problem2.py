'''
Created on Jan 17, 2013

@author: PaymahnMoghadasian
'''
tally = 0
a, b = 0, 1
while a < 4000000:
    print a,
    if a % 2 == 0:
        tally += a
    
    a, b = b, a + b
    
print 
print tally
