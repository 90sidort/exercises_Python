# Description: https://www.codewars.com/kata/5800b6568f7ddad2c10000ae
# Short task summary:
##
##Task
##
##Given a positive integer as input, return the output as a string in the following format:
##
##Each element, corresponding to a digit of the number, multiplied by a power of 10 in such a way that with the sum of these elements you can obtain the original number.

# My solution:
def simplify(number):
    if number == 0:
        return ""
    number = str(number)
    lngth = len(number)
    equation = ''
    for i in range (lngth):
        if number[i] != '0':
            zeroes = '1' + ((lngth - 1) * '0') if lngth > 1 else ''
            equation = equation + number[i] + '*' + zeroes + '+' if lngth > 1 else equation + number[i] 
        lngth -= 1
    return equation if equation[-1] != '+' else equation[:-1]
