# Description: https://www.codewars.com/kata/598d89971928a085c000001a
# Short task summary:
##About the replacement
## Choose exactly one element from the sequence and replace it with another integer > 0. It is not allowed to replace a number with itself or to change no number at all.
##
##Task
## Find the minimal possible sequence after performing a valid replacement and sorting the sequence.
##
##Input:
## Input contains sequence with N integers. All elements of the sequence > 0. The sequenc will never be empty.
##
##Output:
## Return sequence with N integers — the minimum possible values of each sequence element after one replacement and the sorting are performed.
# My solution:
def sort_number(a):
    a[a.index(max(a))] = 1 if max(a) > 1 else 2
    return sorted(a)
