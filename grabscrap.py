# Description: https://www.codewars.com/kata/52b305bec65ea40fe90007a7
# My solution:
def grabscrab(word, possible_words):
    output_words = []
    for w in possible_words:
        for c in w:
            if w.count(c) != word.count(c):
                is_ok = False
                break
            else:
                is_ok = True
        if is_ok == True and set(word) == set(w):
            output_words.append(w)
    return output_words