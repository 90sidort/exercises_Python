# Description: https://www.codewars.com/kata/59da47fa27ee00a8b90000b4
# My solution:
def solve(s):
    s = list(s)
    counter = 0
    for x in range(0, len(s)):
        temp_s = s[x]
        if int(temp_s) % 2:
            counter += 1
        for y in range(x+1, len(s)):
            temp_s += s[y]
            if int(temp_s) % 2:
                counter += 1
    return counter