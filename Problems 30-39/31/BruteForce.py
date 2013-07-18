'''
Created on Jan 21, 2013

@author: PaymahnMoghadasian
'''
DESIRED_SUM = 200

coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

used_combinations = set()

def recurse(curr_combination):
    # print "Entering recurse"
    # print curr_combination
    if curr_combination in used_combinations:
        return 0
    
    used_combinations.add(curr_combination)
    curr_sum = 0
    curr_combination = [int(x) for x in curr_combination.split(',')]
    for i in range(len(coin_values)):
        curr_sum += curr_combination[i] * coin_values[i]
    
    
    # curr_sum = sum([int(curr_combination[x]) * coin_values[x] for x in range(len(coin_values))]) 
    if curr_sum == DESIRED_SUM:
        return 1
    
    if curr_sum > DESIRED_SUM:
        return 0
    
    # find all combinations from this point forward
    num_combinations = 0
    for i in range(len(coin_values)):
        curr_combination[i] += 1
        num_combinations += recurse(','.join(map(str, curr_combination)))
        curr_combination[i] -= 1
        
    return num_combinations


print recurse(('0,0,0,0,0,0,0,0'))
