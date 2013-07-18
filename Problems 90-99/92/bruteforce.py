count = 0
# to_89 = set()
for i in range(1, 10000000):
    next_num = i
    while next_num != 1 and next_num != 89:
        next_num = sum([int(x) ** 2 for x in str(next_num)])

    if next_num == 89:
        count += 1
        # to_89.add(i)

# print (len(to_89))
print (count)
