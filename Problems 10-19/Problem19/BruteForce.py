'''
Created on Jan 19, 2013

@author: PaymahnMoghadasian
'''
'''
http://gmmentalgym.blogspot.de/2011/03/day-of-week-for-any-date-revised.html#ndatebasics
'''

month_code = {1:6, 2:2, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
leap_year_codes = {2000:0, 2004:5, 2008:3, 2012:1, 2016:6, 2020:4, 2024:2}

def find_year_value(year):
    print "Check year ", year
    if year % 4 == 0:
        if leap_year_codes.has_key(year):
            return leap_year_codes[year]
        
        if (year % 100) % 12 == 0:
            return (year % 100) / 12
        else:
            return find_year_value(2000 + (year % 100) % 28)
    else:
        return (year % 4 + find_year_value(year - year % 4)) % 7
        
def find_month_value(month):
    if year % 4 == 0 and (month == 1 or month == 2):
        return month_code[month] - 1
    else:
        return month_code[month]


count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        last_two = year % 100
        if year < 2000: 
            y_value = find_year_value(year + 100)
        else:
            y_value = find_year_value(year)
            
        month_value = find_month_value(month)
        
        day = (y_value + month_value + 1) % 7
        if year < 2000:
            day = (day + 1) % 7
            
        
        if 0 == day:
            count += 1

print count
        
