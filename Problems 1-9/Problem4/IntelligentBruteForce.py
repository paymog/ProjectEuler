'''
Created on Jan 17, 2013

@author: PaymahnMoghadasian
'''

'''
999**2 is a 6 digit number

A six digit palindrome can be expressed as:
    100000a + 10000b + 1000c + 100c + 10b + a 
=   100001a + 10010b  + 1100c
=   11(9091a + 910b + 100c)

Therefore, the largest palindrom must divisible by 11

'''

def check_for_divisors(num):
    for i in reversed(range(100, 1000)):
        if num % i == 0 and len(str(num / i)) == 3:
            print "Divisor is ", i
            return True
        
    return False

found = False
for a in reversed(range(1, 10)):
    for b in reversed(range(10)):
        for c in reversed(range(10)):
            candidate = 11 * (9019 * a + 910 * b + 100)
            found = check_for_divisors(candidate)
            
            if found:
                break;
        if found:
            break
    if found:
        break
    
print "The result is ", candidate

# HOLD ON, I think this is the same as my other one. Just a different approach to generating the palindromes.
# IF this is faster, then it's marginally faster
