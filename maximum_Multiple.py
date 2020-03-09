# Description: https://www.codewars.com/kata/5aba780a6a176b029800041c
# My solution:
def max_multiple(divisor, bound):
    for x in range(bound, 0, -1):
        if x % divisor == 0:
            return x