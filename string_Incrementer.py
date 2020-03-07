# Description: https://www.codewars.com/kata/54a91a4883a7de5d7800009c
# My solution:
def increment_string(strng):
    num = ''
    first_char = 0
    for c in range(len(strng)-1, -1, -1):
        if strng[c].isdigit():
            num += strng[c]
        else:
            first_char = c + 1
            break
    if num == '':
        return strng + '1'
    else:
        num = num[::-1]
        new_num = "%%0%ii" % len(num) % (int(num)+1)
    return strng[:first_char] + new_num