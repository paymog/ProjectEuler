'''
Created on 2013-01-23

@author: paymahn
'''

last_10 = 10**10

sum = 0
for i in range(1,1001):
    curr = i
    for k in range(2,i+1):
        curr = (curr*i) % last_10
    
    sum = (sum + curr) % last_10

print sum