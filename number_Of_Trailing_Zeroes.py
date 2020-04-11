# Description: https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
# Short task summary:
##Write a program that will calculate the number of trailing zeros in a factorial of a given number.
##
##N! = 1 * 2 * 3 * ... * N
##
##Be careful 1000! has 2568 digits...
##
##For more info, see: http://mathworld.wolfram.com/Factorial.html
##Examples
##
##zeros(6) = 1
### 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
##
##zeros(12) = 2
### 12! = 479001600 --> 2 trailing zeros
# My solution:
def zeros(n):
    fivePower = 5
    howManyFives = 0
    i = 2
    while fivePower < n:
        howManyFives += n // fivePower
        fivePower = 5 ** i
        i += 1
    return howManyFives
