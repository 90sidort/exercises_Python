# Description: https://www.codewars.com/kata/52774a314c2333f0a7000688
# My solution:
def valid_parentheses(string):
    count = 0
    for x in string:
        if x == '(':
            count += 1
        if x == ')':
            count -= 1
        if count < 0:
            return False
    return True if count == 0 else False