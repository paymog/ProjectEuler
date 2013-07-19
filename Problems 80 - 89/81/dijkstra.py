SIZE = 80

matrix = [None] * SIZE
f = open("matrix.txt")
for i in range(SIZE):
    matrix[i] = [int(x) for x in f.readline().split(",")]

graph = [{} for i in range(SIZE ** 2)]
for i in range(SIZE):
    for j in range(SIZE):
        index = i * SIZE + j
        if i < SIZE - 1:
            graph[index][index + SIZE] = matrix[i + 1][j]
        if j < SIZE - 1:
            graph[index][index + 1] = matrix[i][j + 1]

# run dijkstra
# this is "dist" in the pseudocode on wikipedia
final_distance = [float("inf")] * SIZE ** 2
final_distance[0] = 0

# this combines "dist" and Q in the pseudocode on wikipedia
# hopefully this combination speeds things up. It certainly simplifies
# the search done on line 12 in the pseudocode
dist = {i: final_distance[i] for i in range(len(final_distance))}

while len(dist) > 0:
    current = min(dist, key=dist.get)
    if dist[current] == float("inf"):
        break

    for neighbour in graph[current]:

        alt = dist[current] + graph[current][neighbour]
        if alt < final_distance[neighbour]:
            dist[neighbour] = alt
            final_distance[neighbour] = alt
    
    del dist[current]


print final_distance[end] + matrix[0][0]
