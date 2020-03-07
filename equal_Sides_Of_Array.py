# Description: https://www.codewars.com/kata/5679aa472b8f57fb8c000047
# My solution:
def find_even_index(arr):
    current_index = 1
    if sum(arr[1:len(arr)]) == 0:
        return 0
    while current_index < len(arr):
        left_side_sum = sum(arr[0:current_index])
        right_side_sum = sum(arr[(current_index +1):len(arr)])
        if left_side_sum == right_side_sum:
            return current_index
        current_index += 1
    return -1