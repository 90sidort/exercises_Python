# Description: https://www.codewars.com/kata/55c04b4cc56a697bb0000048
# My solution:
from collections import Counter
def scramble(s1, s2):
    s1set = Counter(s1)
    s2set = Counter(s2)
    for c, count in s2set.items():
        if count > s1set[c]:
            return False
    return True