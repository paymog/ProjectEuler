'''
Created on Jan 17, 2013

@author: PaymahnMoghadasian
'''
print 999 ** 2  # 6 digits long - there are 900 (9*10*10) palindromic 6 digit numbers
print 100 ** 2  # 5 digits long - there are 900 palindromic 5 digit numbers

# there are 1800 candidate numbers. We can probably just check the 6 digit ones

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
            candidate = int("%d%d%d%d%d%d" % (a, b, c, c, b, a))
            
            if candidate <= 999 ** 2:
                found = check_for_divisors(candidate)
            
            if found:
                break;
        if found:
            break
    if found:
        break
    
print "The result is ", candidate
