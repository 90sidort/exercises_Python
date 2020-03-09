# Description: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
# My solution:
def persistence(n):
    n = list(str(n))
    i = 0
    while len(n) > 1:
        suma = 1
        for x in n:
            suma = suma * int(x)
        n = list(str(suma))
        i += 1
    return i