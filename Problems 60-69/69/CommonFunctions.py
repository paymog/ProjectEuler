'''
Created on Jan 18, 2013

@author: PaymahnMoghadasian
'''
import math


def is_prime(num, primes=None):
    root = num ** 0.5
    
    if primes==None:
        primes = sieve_of_Erastothenes(int(root))
        
    for n in primes:
        if num % n == 0:
            return False
        if n > root:
            return True
        
    return True

def Miller_Rabin_primality_test(n):
    '''
    Basically a copy-paste from http://rosettacode.org/wiki/Miller-Rabin_primality_test#Python
    n  < 341,550,071,728,321
    '''
    if n == 2:
        return True
    
    if n%2 == 0 or n < 3:
        return False
    
    d = n -1#d is guaranteed to be even
    tests = [2,3,5,7,11,13,17]
    s = 0
    
    while d%2 == 0:
        s += 1
        d /= 2
    
    assert (2**s * d == n - 1)
    
    
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
    
    for a in tests:
        if a < n and try_composite(a):
            return False
                
    return True


def sieve_of_Erastothenes(n):
    '''Using the sieve of Eratosthenes'''
    sieve = [False] * ((n - 1) / 2 + 1)  # off by one issue without the +1
    root = (int(n ** 0.5) - 1) / 2
    
    for n in range(1, root + 1):
        if not sieve[n]:
            for j in range(2 * n * (n + 1), len(sieve), 2 * n + 1):
                sieve[j] = True
    
    primes = [2]
    for n in range(1, len(sieve)):
        if not sieve[n]:
            primes.append(2 * n + 1)
          
    return primes

def generate_reptend_primes(n):
    primes = sieve_of_Erastothenes(n)
    reptend_primes = []
    for n in primes:
        if 10 ** (n - 1) % n == 1:
            reptend = True
            for j in range(1, n - 1):
                if 10 ** j % n == 1:
                    reptend = False
                    break
            if reptend:
                reptend_primes.append(n)
                
    return reptend_primes

def generate_n_primes(n):
    primes = [2]
    next_num = 3
    while len(primes) < n:
        if is_prime(next_num, primes):
            primes.append(next_num)
            
        next_num += 2  # primes must be odd
            
    return primes

def generate_triangulars(upper, lower=0):
    triangulars = []
    n = 1
    next_num = 1 #the first triangular number
    while next_num <= upper:
        triangulars.append(next_num)
        n += 1
        next_num = n*(n + 1) / 2
        
    return [x for x in triangulars if x >= lower]

def generate_squares(upper, lower=0):
    squares = []
    n = 1
    next_num = 1 #the first triangular number
    while next_num <= upper:
        squares.append(next_num)
        n += 1
        next_num = n*n
        
    return [x for x in squares if x >= lower]

def generate_pentagonals(upper, lower=0):
    pentagonals = []
    n = 1
    next_num = 1 #the first pentagonal number
    while next_num <= upper:
        pentagonals.append(next_num)
        n += 1
        next_num = n*(3*n - 1) / 2
        
    return [x for x in pentagonals if x >= lower]

def generate_hexagonals(upper, lower=0):
    hexagonals = []
    n = 1
    next_num = 1 #the first triangular number
    while next_num <= upper:
        hexagonals.append(next_num)
        n += 1
        next_num = n*(2*n - 1)
        
    return [x for x in hexagonals if x >= lower]

def generate_heptagonals(upper, lower=0):
    heptagonals = []
    n = 1
    next_num = 1 #the first triangular number
    while next_num <= upper:
        heptagonals.append(next_num)
        n += 1
        next_num = n*(5*n - 3)/2
        
    return [x for x in heptagonals if x >= lower]

def generate_octagonals(upper, lower=0):
    octagonals = []
    n = 1
    next_num = 1 #the first triangular number
    while next_num <= upper:
        octagonals.append(next_num)
        n += 1
        next_num = n*(3*n - 2)
        
    return [x for x in octagonals if x >= lower]

def is_triangular(num):
    return is_square(8*num + 1)

def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
        
    return True

def is_pentagonal(num):
    return ((1 + math.sqrt(24*num + 1)) / 6).is_integer() and int(math.sqrt(24*num + 1)) % 6 == 5

def is_hexagonal(num):
    return is_square(8*num + 1) and (int((8*num + 1)**0.5) + 1) % 4 == 0

def is_heptagonal(num):
    return is_square(40*num + 9) and (int((40*num + 9)**0.5) + 3) % 10 == 0

def is_octagonal(num):
    return is_square(3*num + 1) and (int((3*num + 1)**0.5) + 1) % 3 == 0

def generate_n_pentagonals(num):
    pentagonals = []
    
    n= 1
    while len(pentagonals) < num:
        pentagonals.append(n*(3*n - 1) / 2)
        n += 1
        
    return pentagonals
    

def find_divisors(n):
    root = int(round(math.sqrt(n)))
    divisors = []
    
    for n in range(1, root + 1):
        if n % n == 0:
            if n not in divisors:
                divisors.append(n)
            
            if n / n not in divisors:
                divisors.append(n / n)
                
                
    return divisors

def binary_search(array, target):
    begin = 0
    end = len(array)
    mid = None
    result = -1
    
    if target > array[-1] or target < array[0]:
        return result
    
    while begin <= end and result == -1 and begin < len(array):
        mid = (begin + end) / 2
        
        if mid >= len(array):
            print mid
        
        if array[mid] == target:
            result = mid
        elif array[mid] < target:
            begin = mid + 1
        else:
            end = mid - 1
            
    return result
        

def is_palindrome(num):
    num = str(num) #make sure we actually test a num
    
    return num == num[::-1]


def contains_even_digit(num):
    while num > 0:
        if num % 2 == 0:
            return True
        num /= 10
        
    return False

def is_pandigital(num, n):
    
    #if n > 10, 0 is a valid digit, otherwise it isn't
    #for example, n=14 is a number that has everything from 0-4
    #while just 4 allows 1-4
    #likewise, 19 allows 0-9 while 9 allows 1-9
    #n=10 or n < 1 or n > 19 is invalid 
    
    if n ==10 or n < 1 or n >19:
        raise ValueError("N must be between 1 and 9 or 11 and 19")
    
    num_length = int(math.log10(num)) + 1
    upper = n % 10
    allow_zero = n > 10
    
    if num_length != upper:
        return False
    
    if allow_zero:
        digits = [0] * (upper + 1)
    else:
        digits = [0] * upper  
        
    while num > 0:
        
        digit = num % 10 #extract the rightmost digit
        if (not allow_zero and digit < 1) or digit > upper:
            return False
        
        digits[digit-1] += 1
        if digits[digit-1] > 1:
            return False
        
        num /= 10 #pull off the rightmost digit 1234 -> 123
        
    for n in digits:
        if n != 1:
            return False
        
    return True


def tuple_to_num(tup):
    result = 0
    for n in tup:
        result *= 10
        result += int(n)
        
    return result

def find_prime_factors(num, primes=None):
    if primes == None:
        primes = sieve_of_Erastothenes(num)
    factors = {} #factor:number of times
    
    n = 0
    while primes[n] <= num**0.5 and num > 1:
        if num%primes[n] == 0:
            factors[primes[n]] = 0
            while num > 1 and num% primes[n] == 0:
                factors[primes[n]] += 1
                num /= primes[n]
        n += 1
          
    if primes[n] > num**0.5 and num > 1:
        factors[num] = 1
        
                
    return factors


def has_repeat_digits(num, num_repeated_digits):
    digits = [0] * 10
    
    while num > 0:
        digits[num % 10] += 1
        num /= 10
        
    for n in digits:
        if n == num_repeated_digits:
            return True
        
    return False

def sum_digits(num):
    tally = 0
    while num > 0:
        tally += num % 10
        num /= 10
        
    return tally

def eulers_totient(num, factors=None, sieve=None):
    
    if factors is None:
        if sieve is None:
            sieve = sieve_of_Erastothenes(num)

        factors = find_prime_factors(num, sieve)

    phi = num
    for key in factors:
        val = 1 -  float(1)/key
        phi = phi* (1 - float(1) / key)

    return phi
