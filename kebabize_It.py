# Description: https://www.codewars.com/kata/57f8ff867a28db569e000c4a
# My solution:
import string
import re
def kebabize(strg):
    strg = "".join(re.split("[^a-zA-Z]*", strg))
    new_string = ''
    for x in range(len(strg)):
        if strg[x] in string.ascii_uppercase and x != 0:
            new_string = new_string + '-' + strg[x].lower()
        elif strg[x] in string.ascii_uppercase and x == 0:
            new_string = new_string + strg[x].lower()
        else:
            new_string += strg[x]
    return new_string