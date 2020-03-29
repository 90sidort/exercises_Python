# Description: https://www.codewars.com/kata/5340298112fa30e786000688/python
# Short task summary:

##The objective is to return all pairs of integers from a given collection of integers that have a difference of 2.
##
##The result should be sorted in ascending order.
##
##The input will consist of unique values. The order of the integers in the input collection should not matter.



# My solution:
def twos_difference(lst):
    result = []
    lst.sort()
    for x in lst:
        if (x + 2) in lst:
            add = (x, x+2)
            result.append(add)
    return result
