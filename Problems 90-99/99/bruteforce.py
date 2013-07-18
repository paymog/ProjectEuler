from math import log10
maxnum = 0
maxindex = -1
for i, line in enumerate(open("file.txt").readlines()):
    #print line
    nums = line.split(',')
    base = int(nums[0])
    exp = int(nums[1])
    num = exp * log10(base)
    if num > maxnum:
        maxnum = num
        maxindex = i
print maxindex  



