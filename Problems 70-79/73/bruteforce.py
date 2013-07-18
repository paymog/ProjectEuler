# this is way too slow

from fractions import Fraction
from math import ceil, floor

fractions = set()

for denom in range(1, 9):
    # if denom % 1000 == 0:
    #     print "testing %d" % denom
    print "denom is %d" % denom
    lower = int(ceil((denom + 1)/3))
    upper = int(floor((denom -1) / 2))
    print "\tlower is %d" % lower
    print "\tupper is %d" % upper

    for num in range(lower, upper):
        print "\tnum is %d" % num
        fractions.add(Fraction(num, denom))

print "Converting to list"
fractions = list(fractions)
print len(fractions)
print fractions
# print "Sorting"
# fractions = sorted(fractions)
# print "Finding"
# i1 = fractions.index(Fraction(1,3))
# i2 = fractions.index(Fraction(1,2))

# fractions = fractions[i1 + 1: i2]
# print len(fractions)
# print fractions