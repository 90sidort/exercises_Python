# Description: https://www.codewars.com/kata/5b1b27c8f60e99a467000041
# My solution:
def anagram_difference(w1, w2):
    w1, w2 = list(w1), list(w2)
    common = 0
    for c in range(len(w1)):
        if w1[c] in w2:
            common += 1
            w2[w2.index(w1[c])] = w1[c].upper()
    return (len(w1) + len(w2)) - (common * 2)