MAX = 2001  # this max was determined by using wolfram to solve x choose 2 = 2e6
            # and taking the ceiling of the solution for x. We know that a rectangle
            # of dimensions 2001x1 will have just over 2e6 rectangles within it

# this cache solution works because we know that r will never be greater
# than 2 and so we can cache the solutions when r=2. When r=1 we know
# that the result of n choose 1 is n.
def nCr(n, r, cache):
    if r == 1:
        return n

    if n < 2:
        return 0

    if cache[n] is not None:
        return cache[n]

    result = nCr(n - 1, r, cache) + nCr(n - 1, r - 1, cache)
    cache[n] = result
    return result


cache = [None] * (MAX + 1)
closest = 2e6
bestArea = -1
for i in range(1, MAX):
    for j in range(i, MAX):
        # find out how many rectangles fit in this width and height
        # this way of determining the number of rectangles was found
        # with a quick google
        numRect = nCr(i + 1, 2, cache) * nCr(j + 1, 2, cache)

        # find out if the this many rectangles is closer to 2e6 than the previous
        # best. If so, update
        diff = abs(numRect - 2e6)
        if diff < closest:
            closest = diff
            bestArea = i * j

print bestArea
