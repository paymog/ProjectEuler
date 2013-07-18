'''
Created on Jan 18, 2013

@author: PaymahnMoghadasian
'''

'''
By Euclid we know:

a = m**2 - n**2
b = 2 * m * n
c = m**2 + n**2

for some m > n > 0 such that a < b

------

NOTE: 

if exactly one of m,n is even and gcd(m,n) = 1 then (a,b,c) is a primitive triplet

a = (m**2 - n**2 ) * d
b = 2 * m * n * d
c = (m**2 + n**2) * d

When d = 1, (a,b,c) are primitive

-----
        

We also know that a + b + c = s

Therefore:

(m**2 - n**2) * d + 2*m*n*d + (m**2 + n**2)*d = s
2*m**2*d + 2*m*n*d = s
2*m*d*(m + n) = s
m*d*(m+n) = s/2

From this we can deduce that s/2 % m == 0
We know that since exactly one of m,n is even then m+n must be odd therefore m+n % 2 == 1 and s/(2*m) % (m+n) == 0
let k = m+n

For some reason m < k < 2*m and gcd(m,k) = 1

Once we find an m and k that satisfy the above condidtions then we can determine the triplet
'''
import CommonFunctions as cf
 
s = 120
s2 = s / 2

for m in range(1, int(s2 ** 0.5)):  # we can determine all divisors of s2 by looping up to it's square root
    if s2 % m == 0:  # check that m is a divisor of s/2
        s2m = s2 / m
        
        # k must be odd and larger than m
        if m % 2 == 0:
            k = m + 1
        else:
            k = m + 2
        
        # loop over potential values of k
        while k < 2 * m and k <= s2m ** 0.5:
            # condiditions for k
            if s2m % k == 0 and cf.gcd(k, m) == 1:
                d = s2 / k / m
                n = k - m
                a = (m ** 2 - n ** 2) * d
                b = 2 * m * n * d
                c = (m ** 2 + n ** 2) * d
                
                print "a = %d, b = %d, c = %d, a*b*c = %d" % (a, b, c, a * b * c)
            
            k += 2
                

    
    
