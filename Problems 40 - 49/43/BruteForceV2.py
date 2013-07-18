'''
Created on 2013-01-22

@author: paymahn
'''
import CommonFunctions as cf



def solve(num,remaining):
    #base case.
    #Recheck that the number is valid
    if len(num) == 10 and len(remaining) == 0:
        valid = True
        primes = cf.generate_primes_less_than(20)
        #this loop makes sure that each candidate substring is divisible by 
        #the prime as defined by the problem (d2d3d4 % 2 == 0 and d3d4d5 %3 == 0, etc...)
        for j in range(1,7):
            substr = num[j:j+3]
            prime = primes[j-1]
            if int(substr) % prime != 0:
                valid = False
                break
        
        #if indeed we pass the check, return the number
        if valid:
            return int(num)
        else:
            return 0
    
    #as we flesh out the number, make sure it's valid before we move onto
    #further ones.
    sum = 0
    for i in range(len(remaining)):
        temp = num + remaining[i]
        length = len(temp)
        if temp[0] != '0' and (length < 4 or
                               length == 4 and int(temp[3]) % 2 == 0 or
        length == 5 and int(temp[2:5]) % 3 == 0 or
        length == 6 and int(temp[3:6]) % 5 == 0 or
        length == 7 and int(temp[4:7]) % 7 == 0 or
        length == 8 and int(temp[5:8]) % 11 == 0 or
        length == 9 and int(temp[6:9]) % 13 == 0 or
        length == 10 and int(temp[7:10]) % 17 == 0):
            sum += solve(temp, remaining[0:i] + remaining[i+1:len(remaining)])
            
    return sum
    


print solve('', '0123456789')
