# Description: https://www.codewars.com/kata/5287e858c6b5a9678200083c
# My solution:
def narcissistic(value):
    value_new = list(str(value))
    base = len(value_new)
    value_end = sum([int(x) ** base for x in value_new])
    return True if value_end == value else False