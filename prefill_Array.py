# Description: https://www.codewars.com/kata/54129112fb7c188740000162
# My solution:
def prefill(n,v=None):
    if type(n) == str:
        if n.isdigit() == True:
            n = int(n)
        else:
            return f"{n} is invalid"
    if n==None:
        return f"{n} is invalid"
    if n <= 0 or n == '0':
        return []
    if v == None:
        return ['undefined']
    if type(n) != int:
        return f"{n} is invalid"
    return n * [v]