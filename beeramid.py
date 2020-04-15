# Description: https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/python
# Short task summary:
##Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's Friday too.
##
##A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25...
##
##Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given the parameters of:
##
##1) your referral bonus, and
##
##2) the price of a beer can
# My solution:
def beeramid(bonus, price):
    x = 0
    sum_x = 0
    while sum_x < bonus// price:
        x += 1
        sum_x += x ** 2
        if sum_x > bonus// price:
            return x - 1
    return x
