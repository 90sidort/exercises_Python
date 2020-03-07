# Description: https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
# My solution:
def max_sequence(arr):
    if all(d < 0 for d in arr):
        return 0
    elif all(d > 0 for d in arr):
        return sum(arr)
    highest_sum = 0
    for x in range(0, len(arr)+1):
        i = 0
        while i < (len(arr)+1):
            current_sum = sum(arr[x:i])
            i += 1
            if current_sum > highest_sum:
                highest_sum = current_sum
    return highest_sum