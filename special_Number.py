# Description: https://www.codewars.com/kata/5a55f04be6be383a50000187
# My solution:
def special_number(number):
    number = list(str(number))
    for x in number:
        if int(x) > 5:
            return 'NOT!!'
    return 'Special!!'