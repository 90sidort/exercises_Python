# Description: https://www.codewars.com/kata/5274e122fc75c0943d000148
# My solution:
def group_by_commas(n):
    n = list(str(n))
    if len(n) > 3:
        for x in range(len(n)-3, 0, -3):
            n.insert(x, ',')
    return "".join(n)