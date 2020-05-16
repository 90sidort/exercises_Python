# Description: https://www.codewars.com/kata/5a262cfb8f27f217f700000b
# Short task summary:

##In this Kata, you will be given two strings a and b and your task will be to return the characters that are not common in the two strings.
##
##For example:
##
##solve("xyab","xzca") = "ybzc" 
##--The first string has 'yb' which is not in the second string. 
##--The second string has 'zc' which is not in the first string. 
##Notice also that you return the characters from the first string concatenated with those from the second string.
##
##More examples in the tests cases.
##
##Good luck!

# My solution:
def solve(a,b):
    return "".join([lett for lett in a if lett not in b]) + "".join([lett for lett in b if lett not in a])
