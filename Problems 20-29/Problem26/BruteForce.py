'''
Created on Jan 20, 2013

@author: PaymahnMoghadasian
'''
from test.test_iterlen import len

def divide(numerator, denominator, detect_repetition=True, digit_limit=None):

    # If repetition detection is off, you must 
    # specify a limit on the digits returned 
    if not detect_repetition and digit_limit == None:
        return None

    decimal_found = False
    
    # prime the loop
    v = numerator // denominator
    numerator = 10 * (numerator - v * denominator)
    answer = str(v)
    
    if numerator == 0:
        return answer
    
    answer += '.'
    
    # Maintain a list of all the intermediate numerators 
    # and the length of the output at the point where that 
    # numerator was encountered. If you encounter the same 
    # numerator again, then the decimal repeats itself from 
    # the last index that numerator was encountered at. 
    states = {}
    
    while numerator > 0 and (digit_limit == None or digit_limit > 0):
        # print numerator
        if detect_repetition:
            
            prev_state = states.get(numerator, None)
            if prev_state != None:
                start_repeat_index = prev_state
                non_repeating = answer[:start_repeat_index]
                repeating = answer[start_repeat_index:]
                return non_repeating + '[' + repeating + ']'
            
            states[numerator] = len(answer)
        
        v = numerator // denominator  # floor division. This gets the next digit in the decimal portion
        answer += str(v)  # concatenate next digit to answer
        numerator -= v * denominator  # next two lines do magic
        numerator *= 10
        if digit_limit != None:
            digit_limit -= 1
    
    if numerator > 0:
        return answer + '...'
    return answer


import time
t = time.time()

length_of_longest = 0
index_of_longest = -1

for i in range(1, 1000):
    result = divide(1, i, True, 2000)
    length = result.find(']') - result.find('[')
    if length > length_of_longest:
        length_of_longest = length
        index_of_longest = i
        
print index_of_longest
print time.time() - t

print divide(1, 983, True, 1000)















