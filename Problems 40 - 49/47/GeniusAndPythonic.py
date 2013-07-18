'''
Created on 2013-01-23

@author: paymahn
'''
def PE47(lim=200000,dpf=4):
    sieve=[0]*(lim+1)
    for i in xrange(2,lim/2+1):
        '''
        If i is prime then sieve[i] will be zero
        '''
        if sieve[i]==0:
            '''
            not sure how to explain this part so I'll try to illustrate
            when i=2, we increment everything that has 2 as a factor once
            when i=3, we increment everything that has 3 as a factor once
            when i=p for some prime p, we increment everything that has p as a factor once
            '''
            for j in range(i,lim+1,i): sieve[j]+=1 #unoptimized sieve
            
    
    return ''.join(map(str,sieve)).index(''.join(map(str,[dpf]*dpf)))

print PE47()