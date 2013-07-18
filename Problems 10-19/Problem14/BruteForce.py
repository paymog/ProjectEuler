'''
Created on Jan 18, 2013

@author: PaymahnMoghadasian
'''
from test.test_iterlen import len

found_values = {}

def find_collatz_length(n):
    if n == 1:
        return 1
    elif found_values.has_key(n):
            return found_values[n] 
    else:        
        if n % 2 == 0:
            return 1 + find_collatz_length(n / 2)
        else:
            return 1 + find_collatz_length(3 * n + 1)



largest_seed = 0
largest_length = 0
for i in range(1, 1000000):
    
    length = find_collatz_length(i)
    found_values[i] = length
    # print i, " : ", length
    
    if(length > largest_length):
        largest_seed = i
        largest_length = length
        
print largest_seed
