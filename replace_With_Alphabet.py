# Description: https://www.codewars.com/kata/546f922b54af40e1e90001da
# My solution:
import string
def alphabet_position(text):
    pos = list(string.ascii_lowercase)
    alph_pos = ''
    text = text.lower()
    for x in text:
        if x in pos:
            x_pos = pos.index(x) + 1
            alph_pos = alph_pos + str(x_pos) + ' '
    return alph_pos.strip()