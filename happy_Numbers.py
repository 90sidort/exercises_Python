# Description: https://www.codewars.com/kata/59d53c3039c23b404200007e
# Short task summary:

##Math geeks and computer nerds love to anthropomorphize numbers and assign emotions and personalities to them. Thus there is defined the concept of a "happy" number. A happy number is defined as an integer in which the following sequence ends with the number 1.
##
##    Start with the number itself.
##    Calculate the sum of the square of each individual digit.
##    If the sum is equal to 1, then the number is happy. If the sum is not equal to 1, then repeat steps 1 and 2. A number is considered unhappy once the same number occurs multiple times in a sequence because this means there is a loop and it will never reach 1.
##
##For example, the number 7 is a "happy" number:
##
##72 = 49 --> 42 + 92 = 97 --> 92 + 72 = 130 --> 12 + 32 + 02 = 10 --> 12 + 02 = 1
##
##Once the sequence reaches the number 1, it will stay there forever since 12 = 1
##
##On the other hand, the number 6 is not a happy number as the sequence that is generated is the following: 6, 36, 45, 41, 17, 50, 25, 29, 85, 89, 145, 42, 20, 4, 16, 37, 52, 29
##
##Once the same number occurs twice in the sequence, the sequence is guaranteed to go on infinitely, never hitting the number 1, since it repeat this cycle.
##
##Your task is to write a program which will print a list of all happy numbers between 1 and x (both inclusive), where:
##
##2 <= x <= 5000

# My solution:
def happy_numbers(n):
    hpp_nmbrs = [1]
    for x in range(2,n+1):
        nxt_sqr = []
        crrnt_sqr = x
        while crrnt_sqr != 1:
            nw_sqr = 0
            for d in str(crrnt_sqr):
                nw_sqr += int(d) ** 2
            crrnt_sqr = nw_sqr
            if crrnt_sqr == 1:
                hpp_nmbrs.append(x)
            elif crrnt_sqr not in nxt_sqr:
                nxt_sqr.append(crrnt_sqr)
            else:
                break
    return hpp_nmbrs  
