# Description: https://www.codewars.com/kata/5b1b27c8f60e99a467000041/python
# Short task summary:
##Given two words, how many letters do you have to remove from them to make them anagrams?
##Example
##
##    First word : c od e w ar s (4 letters removed)
##    Second word : ha c k er r a nk (6 letters removed)
##    Result : 10


# My solution:
import string
def anagram_difference(w1, w2):
    count = 0
    for char in string.ascii_lowercase:
        if w1.count(char) != w2.count(char):
            count += w1.count(char) - w2.count(char) if w1.count(char) > w2.count(char) else w2.count(char) - w1.count(char)
    return count
