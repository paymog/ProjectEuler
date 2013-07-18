#there's a bug here. in the first break,
#what if numbers after the current i also
#have a permutation with the target sort?
#it violates the "exactly" requirement of the problem

cubes = {}
target = 3
target_sort = None
upperbound = 10000
for i in range(1,upperbound):
    cube = i**3
    sorted_digits = "".join(sorted(str(cube)))
    if cubes.has_key(sorted_digits):
        cubes[sorted_digits] += 1
        if cubes[sorted_digits] == target:
            print i**3
            target_sort = sorted_digits
            break
    else:
        cubes[sorted_digits] = 1
    

for i in range(1, upperbound):
    cube = i**3
    sorted_digits = "".join(sorted(str(cube)))
    if sorted_digits == target_sort:
        print i**3
        break