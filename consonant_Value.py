# Description: https://www.codewars.com/kata/59c633e7dcc4053512000073
# My solution:
def solve(s):
    current_value = 0
    current_max = 0
    for c in s:
        if c not in 'aeiou':
            current_value = current_value + ord(c) - 96
        else:
            if current_value > current_max:
                current_max = current_value
            current_value = 0
    return current_max