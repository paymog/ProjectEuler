'''
Created on Jan 21, 2013

@author: PaymahnMoghadasian
'''
DESIRED_AMOUNT = 10000

denominations = [1, 2, 5, 10, 20, 50, 100, 200]
cache = [[0 for i in range(DESIRED_AMOUNT + 1)] for j in range(len(denominations))]


def count(remaining_amount, curr_denom):
    if remaining_amount == 0 or curr_denom <= 0:
        return 1
    
    if cache[curr_denom][remaining_amount] > 0:
        return cache[curr_denom][remaining_amount]
    
    num_ways = 0
    temp = remaining_amount
    
    while remaining_amount >= 0:
        num_ways += count(remaining_amount, curr_denom - 1)
        remaining_amount -= denominations[curr_denom]
        
    cache[curr_denom][temp] = num_ways    

    return cache[curr_denom][temp]

print count(DESIRED_AMOUNT, len(denominations) - 1)
