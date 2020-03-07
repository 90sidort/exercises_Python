# Description: https://www.codewars.com/kata/52de553ebb55d1fca3000371
# My solution:
def find_missing(sequence):
    d = (sequence[-1] - (sequence[0])) // len(sequence)
    i = 0
    while i < len(sequence) - 1:
        if sequence[i+1] - sequence[i] != d:
            return sequence[i] + d
        i += 1