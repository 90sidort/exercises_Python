# Description: https://www.codewars.com/kata/5966847f4025872c7d00015b
# My solution:
def average_string(s):
    if len(s) == 0:
        return 'n/a'
    s = s.split()
    valid = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    sums = 0
    for x in s:
        if x in valid:
            sums += valid[x]
        else:
            return "n/a"
    for name, num in valid.items():
        if num == (sums // len(s)):
            return name