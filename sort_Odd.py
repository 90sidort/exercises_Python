# Description: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
# My solution:
def sort_array(source_array):
    temp = sorted([x for x in source_array if x % 2 != 0])
    i = 0
    for y in range(0, len(source_array)):
        if source_array[y] % 2 !=0:
            source_array[y] = temp[i]
            i += 1
    return source_array