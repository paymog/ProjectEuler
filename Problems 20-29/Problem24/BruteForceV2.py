'''
Created on Jan 20, 2013

@author: PaymahnMoghadasian
'''
import itertools as it
import time

tStart = time.time()

permutations = [reduce(lambda rst, d: rst * 10 + d, x) for x in it.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]

permutations.sort()

print permutations[999999]

print time.time() - tStart
