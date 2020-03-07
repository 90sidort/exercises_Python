# Description: https://www.codewars.com/kata/5b39e3772ae7545f650000fc
# My solution:
def remove_duplicate_words(s):
    s = s.split()
    s_new = ''
    for x in s:
        if x not in s_new:
            s_new = s_new + x + ' '
    return s_new.strip()