# Description: https://www.codewars.com/kata/59b72376460387017e000062
# My solution:
def is_hollow(x):
    if len(x) < 3:
        return False
    middle = len(x) // 2
    zeroes =  True if (x[middle] + x[middle-1] + x[middle+1]) == 0 else False
    left = [d1 for d1 in x[:middle-1] if d1 != 0]
    right = [d2 for d2 in x[middle+2:] if d2 != 0]
    even = True if (len(left) == len(right)) else False
    return zeroes and even