# Description: https://www.codewars.com/kata/57a6633153ba33189e000074
# Short task summary:

##Count the number of occurrences of each character and return it as a list of tuples in order of appearance. For empty output return an empty list.
##
##Example:
##
##ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
# My solution:
def ordered_count(inp):
    result = []
    used = []
    for char in inp:
        if char not in used:
            result.append((char, inp.count(char)))
            used.append(char)
    return result
