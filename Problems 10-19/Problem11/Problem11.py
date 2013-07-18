'''
Created on Jan 18, 2013

@author: PaymahnMoghadasian
'''
from numpy.core.fromnumeric import product as prod
NUM_ADJACENT = 4

def read_file(name):
    f = open(name)
    
    line = f.readline()
    elements = line.split(' ')
    grid = [[] for i in range(len(elements))]
    curr_row = 0
    while line:
        for i in range(len(elements)):
            grid[curr_row].append(int(elements[i]))
        
        line = f.readline()
        elements = line.split(' ')
        curr_row += 1
    
    return grid
    pass

def find_largest_horizontal_product(grid):
    largest = 0
    for i in range(len(grid)):
        for j in range(len(grid[i]) - (NUM_ADJACENT - 1)):
            
            temp = prod(grid[i][j:j + NUM_ADJACENT]) 
            if temp > largest:
                largest = temp
            pass
    
    return largest

def find_largest_vertical_product(grid):
    largest = 0
    for i in range(len(grid) - (NUM_ADJACENT - 1)):
        for j in range(len(grid[i])):
            
            temp = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
            if temp > largest:
                largest = temp
            pass
    
    return largest
    pass

def find_largest_diagonal_product_forwards(grid):
    largest = 0
    for i in range(len(grid) - (NUM_ADJACENT - 1)):
        for j in range(len(grid[i]) - (NUM_ADJACENT - 1)):
            
            temp = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
            if temp > largest:
                largest = temp
            pass
    
    return largest

def find_largest_diagonal_product_backwards(grid):
    largest = 0
    for i in reversed(range(NUM_ADJACENT - 1 , len(grid))):
        for j in range(len(grid[i]) - (NUM_ADJACENT - 1)):
            
            temp = grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
            if temp > largest:
                largest = temp
            pass
    
    return largest
    pass

grid = read_file("grid.txt")
largest = find_largest_horizontal_product(grid)

temp = find_largest_vertical_product(grid)
if temp > largest:
    largest = temp

temp = find_largest_diagonal_product_forwards(grid)
if temp > largest:
    largest = temp

temp = find_largest_diagonal_product_backwards(grid)
if temp > largest:
    largest = temp
    
print largest
