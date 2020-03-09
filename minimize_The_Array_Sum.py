# Description: https://www.codewars.com/kata/5a523566b3bfa84c2e00010b
# My solution:
def min_sum(arr):
    arr = sorted(arr)
    multi_sum = 0
    for x in range(0, int((len(arr)/2))):
        multi_sum = multi_sum + (arr[x] * arr[(-1)*(x+1)])
    return multi_sum