'''
Created on Jan 26, 2013

@author: PaymahnMoghadasian
'''
'''
Use frequency analysis
'''

cryptotext = [int(x) for x in open('cipher.txt').read().split(',')]

char1 = [0]*256
char2 = [0]*256
char3 = [0]*256

i = 0
while i < len(cryptotext):
    if i % 3 == 0:
        char1[cryptotext[i]] += 1
    elif i % 3 == 1:
        char2[cryptotext[i]] += 1
    else:
        char3[cryptotext[i]] += 1
    
    i += 1
    
mc1 = char1.index(max(char1))
mc2 = char2.index(max(char2))
mc3 = char3.index(max(char3))

k1 = mc1 ^ ord(' ')
k2 = mc2 ^ ord(' ')
k3 = mc3 ^ ord(' ')

key = k1+k2+k3
plaintext = [None] * len(cryptotext)
i = 0
while i < len(cryptotext):
    if i % 3 == 0:
        plaintext[i] = k1 ^ cryptotext[i]
    elif i % 3 == 1:
        plaintext[i] = k2 ^ cryptotext[i]
    else:
        plaintext[i] = k3 ^ cryptotext[i]
    
    i += 1
    

print sum(plaintext)
        