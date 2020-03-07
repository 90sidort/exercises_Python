# Description: https://www.codewars.com/kata/55eeddff3f64c954c2000059
# My solution:
def sum_consecutives(s):
    previous = None
    result = []
    for d in s:
        if d == previous:
            result[-1] += d
        else:
            result.append(d)
        previous = d
    return result