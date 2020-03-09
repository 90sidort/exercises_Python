# Description: https://www.codewars.com/kata/5467e4d82edf8bbf40000155
# My solution:
def descending_order(num):
    num = list(str(num))
    num = sorted(num, reverse=True)
    num  = "".join(num)
    return int(num)