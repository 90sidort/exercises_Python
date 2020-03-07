# Description: https://www.codewars.com/kata/550498447451fbbd7600041c
# My solution:
def comp(array1, array2):
    if (type(array1) != list) or (type(array2) != list) or (len(array1) != len(array2)):
        return False
    array1 = sorted([x*x for x in array1])
    array2 = sorted(array2)
    for x in range(0, len(array1)):
        if array1[x] != array2[x]:
            return False
    return True