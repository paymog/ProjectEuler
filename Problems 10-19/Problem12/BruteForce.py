'''
Created on Jan 18, 2013

@author: PaymahnMoghadasian
'''
from numpy.lib.scimath import sqrt

def num_divisors(num):
    divisors = 0
    for i in range(1, int(sqrt(num))):
        if num % i == 0:
            divisors += 1
            
    divisors *= 2
    if sqrt(num).is_integer():
        divisors += 1
        
    return divisors


incomplete = True
iteration = 1
curr_tri_num = None

while incomplete:
    curr_tri_num = iteration * (iteration + 1) / 2
    if num_divisors(curr_tri_num) >= 500:
        incomplete = False
        
    iteration += 1
        
print curr_tri_num 
