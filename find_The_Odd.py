# Description: https://www.codewars.com/kata/54da5a58ea159efa38000836
# My solution:
def find_it(seq):
    for x in seq:
        if seq.count(x) % 2 != 0:
            return x