def ways(sums, depth):
    # print "\t".join([""] * depth) + str(sums)
    sum_set = set(sums)
    sum_set = sorted(sum_set, reverse=True)
    first = sum_set[0]
    sum_set = sum_set[1:]
    # print sum_set
    num_ways = 0
    
    for x in sum_set:
        if abs(x - sums[0]) > 1:
            copy = sums[:]
            
            index = copy.index(x)
            copy[0] -= 1
            copy[index] += 1

            num_ways += 1
            num_ways += ways(copy, depth + 1)

    
    return num_ways

VALUE = 50
sums = [0] * VALUE
sums[0] = VALUE
print ways(sums, 0)
