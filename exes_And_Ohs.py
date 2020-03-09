# Description: https://www.codewars.com/kata/55908aad6620c066bc00002a
# My solution:
def xo(s):
    return s.count('o') + s.count('O') == s.count('x') + s.count('X')