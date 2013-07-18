'''
Created on 2013-01-22

@author: paymahn
'''

def find_word_value(word):
    return sum(ord(x) - ord('A') + 1 for x in word)

import time
t = time.time()

tri_nums = set() #set for fast lookup later

for n in range(1,100):
    tri_nums.add(n*(n+1) /2)

count = 0
for word in open('words.txt').read().split(','):
    if find_word_value(word) in tri_nums:
        count += 1
        
print count

print time.time() - t