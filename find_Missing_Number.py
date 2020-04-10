# Description: https://www.codewars.com/kata/5276c18121e20900c0000235/python
# Short task summary:
##Background:
##
##You're working in a number zoo, and it seems that one of the numbers has gone missing!
##
##Zoo workers have no idea what number is missing, and are too incompetent to figure it out, so they're hiring you to do it for them.
##
##In case the zoo loses another number, they want your program to work regardless of how many numbers there are in total.
##Task:
##
##Write a function that takes a shuffled list of unique numbers from 1 to n with one element missing (which can be any number including n). Return this missing number.
##
##Note: huge lists will be tested.

# My solution:
def find_missing_number(numbers):
    if numbers == []:
        return 1
    diff = sum(range(min(numbers), max(numbers)+1)) - sum(numbers)
    if diff == 0 and 1 not in numbers:
        return 1
    elif diff == 0 and 1 in numbers:
        return max(numbers) + 1
    else:
        return diff
