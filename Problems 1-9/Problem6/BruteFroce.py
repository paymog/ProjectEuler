'''
Created on Jan 17, 2013

@author: PaymahnMoghadasian
'''

sum_of_squares = sum(x ** 2 for x in range(1, 101))
square_of_sums = sum(x for x in range(1, 101)) ** 2

print square_of_sums - sum_of_squares
