# this is way too slow

from fractions import Fraction

fractions = set()

for denom in range(1, 1000001):
    # print "testing %d" % denom
    for num in range(denom * 3/7 -3, denom * 3 / 7 + 3):
        fractions.add(Fraction(num, denom))

print "Converting to list"
fractions = list(fractions)
print "Sorting"
fractions = sorted(fractions)
print "Finding"
print fractions[fractions.index(Fraction(3, 7)) - 1]
