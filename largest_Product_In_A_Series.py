# Description: https://www.codewars.com/kata/529872bdd0f550a06b00026e
# Short task summary:

##Complete the greatestProduct method so that it'll find the greatest product of five consecutive digits in the given string of digits.
##
##For example:
##
##greatestProduct("123834539327238239583") // should return 3240
##
##The input string always has more than five digits.
##
##Adapted from Project Euler.



# My solution:
def greatest_product(n):
    high_sum = 0
    curr_cons = ''
    for i in range((len(n)+1)-5):
        current_sum = sum([int(x) for x in n[i:i+5]])
        if current_sum > high_sum and '0' not in n[i:i+5]:
            high_sum = current_sum
            curr_cons = n[i:i+5]
    if curr_cons != '':
        prod = int(curr_cons[0])
        for y in curr_cons[1:]:
            prod = prod * int(y)
        return prod
    else:
        return 0
