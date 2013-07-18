'''
Created on Jan 18, 2013

@author: PaymahnMoghadasian
'''
teens = {10:len('ten'), 11:len('eleven'), 12:len('twelve'),
         13:len('thirteen'), 14:len('fourteen'), 15:len('fifteen'),
         16:len('sixteen'), 17:len('seventeen'), 18:len('eighteen'), 19:len('nineteen')}

ones = {0:0, 1:len('one'), 2:len('two'), 3:len('three'), 4:len('four'), 5:len('five'), 6:len('six'), 7:len('seven'), 8:len('eight'), 9:len('nine')}

tens = {20:len('twenty'), 30:len('thirty'), 40:len('forty'), 50:len('fifty'), 60:len('sixty'), 70:len('seventy'), 80:len('eighty'), 90:len('ninety')}
hundred = 7
aand = 3
count = 0

def less_than_100(i):
    if i < 10:
        return ones[i]
    elif i < 20:
        return teens[i]
    elif i < 100:
        return ones[i % 10] + tens[i - i % 10]



for i in range(1, 1000):
    if i < 100:
        count += less_than_100(i)
    else:
        count += ones[i / 100]
        count += hundred
        count += aand
        count += less_than_100(i % 100)
        
        
print count + ones[1] + len("thousand") - aand * 9  # Overcount and. The word isn't used for 100,200,300....
            
