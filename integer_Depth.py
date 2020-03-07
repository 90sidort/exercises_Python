# Description: https://www.codewars.com/kata/59b401e24f98a813f9000026
# My solution:
def compute_depth(n):
    all_digits = []
    i = 1
    while len(all_digits) < 10:
        result = n * i
        for d in str(result):
            if d not in all_digits:
                all_digits.append(d)
        i += 1
    return i - 1
