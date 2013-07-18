'''
Created on 2013-01-25

@author: paymahn
'''

'''
there's a symmetry in pascals triangle, let's exploit that

'''

SIZE = 101
LIMIT = 10**6
pascals = [[1 for x in range(y+1)] for y in range(SIZE)]

tally = 0
for i in range(2,SIZE):
    for j in range(1,i/2 + 1):
        if i %2==0:
            even = True
        else:
            even = False
        
        sum = pascals[i-1][j] + pascals[i-1][j-1]    
        if sum >= LIMIT:
            sum = LIMIT
        
        if not even and j == i/2:
            pascals[i][j+1] = sum
            
        if sum == LIMIT:
            if not even or j != i/2:
                tally += 2
            else:
                tally += 1
        
        pascals[i][j] = sum
        
print tally
for x in range(len(pascals)):
    print x, ':', pascals[x]