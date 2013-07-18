'''
Created on Jan 19, 2013

@author: PaymahnMoghadasian
'''
import itertools as it

permutations = [int("".join(map(str, x))) for x in it.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]

permutations.sort()

print permutations[999999]
