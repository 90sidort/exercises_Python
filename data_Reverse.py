# Description: https://www.codewars.com/kata/569d488d61b812a0f7000015
# My solution:
def data_reverse(data):
    reversed_arrays = [data[x-8:x] for x in range(len(data), 0 ,-8)]
    reversed_array = []
    for array in reversed_arrays:
        for element in array:
            reversed_array.append(element)
    return reversed_array