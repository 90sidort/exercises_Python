# Description: https://www.codewars.com/kata/57b6f5aadb5b3d0ae3000611
# My solution:
def get_length_of_missing_array(array_of_arrays):
    if len(array_of_arrays) == 0 or None in array_of_arrays or [] in array_of_arrays:
        return 0
    lengths = [len(x) for x in sorted(array_of_arrays)]
    sum_of_all = int((len(lengths) + 1) * ((lengths[0] / 2) + (lengths[-1] / 2)))
    return sum_of_all - sum(lengths)