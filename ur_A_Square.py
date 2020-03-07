# Description: https://www.codewars.com/kata/54c27a33fb7da0db0100040e
# My solution:
def is_square(n):
    if n < 0:
        return False
    nth_root = n**(1/float(2))
    return True if nth_root.is_integer() else False
