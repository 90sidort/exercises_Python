# Description: https://www.codewars.com/kata/59325dc15dbb44b2440000af
# My solution:
def is_alt(s):
    vowels = 'aeiou'
    is_v_or_c = 'vowel' if s[0] in vowels else 'cons'
    for x in range(1,len(s)):
        is_what = 'vowel' if s[x] in vowels else 'cons'
        if is_what == is_v_or_c:
            return False
        else:
            is_v_or_c = is_what
    return True