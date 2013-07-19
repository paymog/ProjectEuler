from time import sleep

SIZE = 80

matrix = [None] * SIZE
f = open("matrix.txt")
for i in range(SIZE):
    matrix[i] = [int(x) for x in f.readline().split(",")]

cache = [[float("inf")]*SIZE for i in range(SIZE)]
#cache[0][0] = matrix[0][0]


def minPath(matrix, start_i, start_j, end_i, end_j):
    if start_i == end_i and start_j == end_j:
        return matrix[end_i][end_j]
    
    if cache[start_i][start_j] != float("inf"):
        return cache[start_i][start_j]

    
    r1 = r2 = float("inf")
    if start_i < end_i - 1:
        r2 = matrix[start_i][start_j] + minPath(matrix, start_i + 1, start_j, end_i, end_j)    
    if start_j < end_j - 1:
        r1 = matrix[start_i][start_j] + minPath(matrix, start_i, start_j + 1, end_i, end_j)
    
    sleep(1)
    cache[start_i][start_j] = min(r1, r2)
    return cache[start_i][start_j]


print minPath(matrix, 0,0,1, 1)