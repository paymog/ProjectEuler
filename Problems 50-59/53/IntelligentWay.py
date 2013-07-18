'''
Created on 2013-01-25

@author: paymahn
'''

'''
Pascals triangle is intimately related to combinations and we can use this fact
to calculate much faster

'''

SIZE = 101
LIMIT = 10**6
pascals = [[1 for x in range(SIZE)] for y in range(SIZE)] 
pascals[0][3] = 4

tally = 0
for i in range(2,SIZE):
    for j in range(1,i):
        sum = pascals[i-1][j] + pascals[i-1][j-1]
        if sum >= LIMIT:
            sum = LIMIT
            tally += 1
        
        pascals[i][j] = sum
        
print tally