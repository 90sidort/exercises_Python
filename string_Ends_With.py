# Description: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
# My solution:
def solution(string, ending):
    return string[-(len(ending)):] == ending if len(ending) > 0 else True