# Description: https://www.codewars.com/kata/567bed99ee3451292c000025
# My solution:
def is_vowel(s):
    return True if len(s) == 1 and s.lower() in 'aeiou' else False