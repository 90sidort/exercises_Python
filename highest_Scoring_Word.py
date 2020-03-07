# Description: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
# My solution:
def high(x):
    array = x.split()
    curr_word = ''
    curr_score = 0
    for word in array:
        score = 0
        for lett in word:
            score = score + (ord(lett) - 96)
        if score > curr_score:
            curr_score = score
            curr_word = word
    return curr_word
