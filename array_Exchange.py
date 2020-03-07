# Description: https://www.codewars.com/kata/5353212e5ee40d4694001114
# My solution:
def exchange_with(a, b):
    a[:], b[:] = b[::-1], a[::-1]