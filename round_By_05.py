# Description: https://www.codewars.com/kata/51f1342c76b586046800002a/python
# Short task summary:
##Round any given number to the closest 0.5 step
##
##I.E.
##
##solution(4.2) = 4
##solution(4.3) = 4.5
##solution(4.6) = 4.5
##solution(4.8) = 5
##
##Round up if number is as close to previous and next 0.5 steps.
##
##solution(4.75) == 5
# My solution:
import math
def solution(n):
    compare = (math.modf(n)[0])
    if compare < 0.25:
        return math.floor(n)
    elif compare >= 0.25 and compare < 0.75:
        return int(str(n).split('.')[0]) + 0.5
    else:
        return math.ceil(n)
