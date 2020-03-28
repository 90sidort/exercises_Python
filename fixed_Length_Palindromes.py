# Description: https://www.codewars.com/kata/59f0ee47a5e12962cb0000bf
# Short task summary:

##Four-digit palindromes start with [1001,1111,1221,1331,1441,1551,1551,...] and the number at position 2 is 1111.
##
##You will be given two numbers a and b. Your task is to return the a-digit palindrome at position b if the palindromes were arranged in increasing order.
##
##Therefore, palin(4,2) = 1111, because that is the second element of the 4-digit palindrome series.
##
##More examples in the test cases. Good luck!



# My solution:
def palin(a,b):
    odd = True if a % 2 != 0 else False
    first_half = ((b-1) + (10 ** (a// 2))) if odd else int((b-1) + (10 ** (a// 2-1))) 
    second_half = str(first_half)[::-1]
    if len(str(first_half)) + len(second_half) > a:
        second_half = second_half[1:]
    return int(str(first_half) + second_half)
