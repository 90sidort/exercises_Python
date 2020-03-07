# Description: https://www.codewars.com/kata/568fca718404ad457c000033
# My solution:
def find(sequence):
    sequence = sorted(sequence)
    d = (sequence[-1] - (sequence[0])) // len(sequence)
    i = 0
    while i < len(sequence) - 1:
        if sequence[i+1] - sequence[i] != d:
            return sequence[i] + d
        i += 1