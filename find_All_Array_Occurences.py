# Description: https://www.codewars.com/kata/59a9919107157a45220000e1
# My solution:
def find_all(array, n):
    return [x for x in range(0, len(array)) if array[x] == n]