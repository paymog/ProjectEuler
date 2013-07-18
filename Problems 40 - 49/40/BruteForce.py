'''
Created on 2013-01-22

@author: paymahn
'''

desired_length = 1000000

i = 1
number = ''

while len(number) < desired_length:
    number += str(i)
    i += 1
    
print int(number[99]) * int(number[999]) * int(number[9999]) * int(number[99999]) * int(number[999999])