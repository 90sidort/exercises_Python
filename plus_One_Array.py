# Description: https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9
# My solution:
def up_array(arr):
  if not arr or min(arr) < 0 or max(arr) > 9:
    return None
  else:
    ans = [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]
    return ans