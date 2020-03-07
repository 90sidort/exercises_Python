# Description: https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004
# My solution:
def highest_rank(arr):
    high = 0
    num = 0
    for i in arr:
        current = arr.count(i)
        if high < current:
            high = current
            num = i
        elif high == current:
            if i > num:
                num = i
    return num