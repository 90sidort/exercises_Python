# Description: https://www.codewars.com/kata/550f22f4d758534c1100025a
# My solution:
def dirReduc(arr):
    while True:
        if arr == []:
            return []
        for x in range(0, len(arr)):
            if x + 1 == len(arr):
                return arr
            elif (arr[x] == 'NORTH' and arr[x+1] == 'SOUTH') or (arr[x] == 'SOUTH' and arr[x+1] == 'NORTH') or (arr[x] == 'WEST' and arr[x+1] == 'EAST') or (arr[x] == 'EAST' and arr[x+1] == 'WEST'):
                del arr[x]
                del arr[x]
                break