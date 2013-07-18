'''
Created on Jan 17, 2013

@author: PaymahnMoghadasian
'''

'''
Note that square of sum = (n*(n+1)/2)^2  
    http://www.wolframalpha.com/input/?i=sum+i+from+i%3D1+to+n&lk=4&num=1 and square this
    
Note that sum of square is = n*(n+1)*(2*n+1)/6
    http://www.wolframalpha.com/input/?i=sum+i%5E2+from+i%3D1+to+n

'''

n = 100

square_of_sum = (n * (n + 1) / 2) ** 2
sum_of_square = n * (n + 1) * (2 * n + 1) / 6

print square_of_sum - sum_of_square
