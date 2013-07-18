'''
Created on Jan 18, 2013

@author: PaymahnMoghadasian
'''

'''
Apparently there's a closed formula for a square grid of size n


'''

cache = {}
HEIGHT = 20
WIDTH = HEIGHT


def maze_tracking(x, y):
    if  x > WIDTH + 1 or y > HEIGHT + 1:
        return 0
    
    if x == WIDTH + 1 and y == HEIGHT + 1:
        return 1
    
    key = str(x) + ',' + str(y)
    if cache.has_key(key):
        return cache[key]
    
    cache[key] = maze_tracking(x + 1, y) + maze_tracking(x, y + 1)
    return cache[key]

print maze_tracking(1, 1)
