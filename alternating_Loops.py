# Description: https://www.codewars.com/kata/55e529bf6c6497394a0000b5/python
# Short task summary:

##Write
##function combine()
##that combines arrays by alternatingly taking elements passed to it.
##E.g
##combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
##combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]) == ['a', 1, 'b', 2, 'c', 3, 4, 5]
##combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]) == ['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5]
##Arrays can have different lengths.


# My solution:
def combine(*args):
    lists = args
    longest = len(max(lists, key=len))
    result = []
    for x in range(longest):
        for y in range(len(lists)):
            try:
                result.append(lists[y][x])
            except:
                pass
    return result
