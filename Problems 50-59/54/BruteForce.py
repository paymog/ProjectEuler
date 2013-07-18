'''
Created on 2013-01-24

@author: paymahn
'''

'''
Fuck this, it's gonna be a ton of code

'''
def compare_card(card):
    value = card[0]
    suit = card[1]
    if value == 'T': value = 10
    elif value == 'J': value = 11
    elif value == 'Q': value = 12
    elif value == 'K': value = 13
    elif value == 'A': value = 14
    else: value = int(value)
    
    value *= 10
    
    if suit == 'S': value += 1
    elif suit == 'C': value += 2
    elif suit == 'D': value += 3
    else: value += 4
    
    return value
        
for line in open('poker.txt').readlines():
    cards = line.split(' ')
    p1_hand = cards[:5]
    p2_hand = cards[5:]
    
    p1_hand.sort(key = compare_card)
    p2_hand.sort(key = compare_card)
    
    
    