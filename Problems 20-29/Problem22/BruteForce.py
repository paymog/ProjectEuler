'''
Created on Jan 19, 2013

@author: PaymahnMoghadasian
'''
names = [x for x in open('names.txt').read().split(',')]
names.sort()
A = ord('A')
tally = 0
for i in range(len(names)):
    n = names[i]
    if n == 'COLIN':
        print i
    tally += sum(ord(n[j]) - A + 1 for j in range(len(n))) * (i + 1)

print tally
print names[936]
