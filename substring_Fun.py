# Description: https://www.codewars.com/kata/565b112d09c1adfdd500019c
# My solution:
def nth_char(words):
    list_words = [words[x][x] for x in range(0, len(words))]
    return "".join(list_words)