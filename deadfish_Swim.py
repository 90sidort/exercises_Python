# Description: https://www.codewars.com/kata/51e0007c1f9378fa810002a9
# My solution:
def parse(data):
    x = 0
    x_ret = []
    for y in data:
        if y == 'i':
            x += 1
        elif y == 'd':
            x -= 1
        elif y == 's':
            x = x**2
        elif y == 'o':
            x_ret.append(x)
    return x_ret