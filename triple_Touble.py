# Description: https://www.codewars.com/kata/55d5434f269c0c3f1b000058/python
# Short task summary:

##Write a function
##
##triple_double(num1, num2)
##
##which takes numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
##
##If this isn't the case, return 0


# My solution:
def triple_double(num1, num2):
    lst1 = list(str(num1))
    num2 = str(num2)
    for i in range(len(lst1)-2):
        if len(set(lst1[i:i+3])) == 1:
            double = 2 * str(lst1[i])
            if double in num2:
                return 1
    return 0
