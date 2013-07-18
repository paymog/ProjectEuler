'''
Created on Jan 21, 2013

@author: PaymahnMoghadasian
'''

'''
9^5 is ~60 000

A 5 digit number is at minimum 10 000 which is < 9^5*5
A 6 digit number is at minimum 100 000 which is < 9^5*6
A 7 digit number is at minimum 1 000 000 which is > 9^5*7

Therefore, 1 000 000 is the upper limit of number we need to check

'''
import time
t = time.time()

tally = 0

for i in range(2, 1000000):
    digits = [ord(x) - 48 for x in str(i)]  # ord(x) - 48 == int(x), ord(x) is much faster though
    if sum(x ** 5 for x in digits) == i:
        tally += i
        
        
print tally

print time.time() - t
