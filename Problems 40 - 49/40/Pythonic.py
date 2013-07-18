'''
Created on 2013-01-22

@author: paymahn
'''

number = ''.join([str(x) for x in range(1,1000000)])
print int(number[99]) * int(number[999]) * int(number[9999]) * int(number[99999]) * int(number[999999])