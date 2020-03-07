# Description: https://www.codewars.com/kata/5544c7a5cb454edb3c000047
# My solution:
def bouncingBall(h, bounce, window):
    if (h <= 0) or (bounce <= 0) or (bounce >= 1) or (window >= h):
        return -1
    else:
        i = 1
        while h > window:
            i += 2
            h = h * bounce
    return i - 2