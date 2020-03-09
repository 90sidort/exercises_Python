# Description: https://www.codewars.com/kata/567de72e8b3621b3c300000b
# My solution:
def is_letter(s):
    if len(s) != 1:
        return False
    else:
        return (ord(s) >= 65 and ord(s) <= 90) or (ord(s) >= 97 and ord(s) <= 122)