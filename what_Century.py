# Description: https://www.codewars.com/kata/52fb87703c1351ebd200081f
# My solution:
def whatCentury(year):
    year = str((int(year) // 100) + 1) if year[1:] != '000' else str((int(year) // 100))
    if int(year[0]) == 1:
        end_str = 'th'
    elif int(year[-1]) == 1:
        end_str = 'st'
    elif int(year[-1]) == 2:
        end_str = 'nd'
    elif int(year[-1]) == 3:
        end_str = 'rd'
    else:
        end_str = 'th'
    return year + end_str