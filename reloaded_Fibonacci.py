# Description: https://www.codewars.com/kata/52549d3e19453df56f0000fe/python
# Short task summary:
##And here is Fibonacci again. This time we want to go one step further. Our fib() function must be faster! Can you do it?
##
##In case you don't know, what the Fibonacci number is:
##
##The nth Fibonacci number is defined by the sum of the two previous Fibonacci numbers. In our case: fib(1) == 0 and fib(2) == 1. With these initial values you should be able to calculate each following Fibonacci number.
##
##Examples:
##
##fib(1) // === 0
##fib(2) // === 1
##fib(3) // === 1
##fib(4) // === 2
##fib(5) // === 3
# My solution:
def fib(n):
    frst = 0
    scnd = 1
    if n == 1:
        return frst
    elif n == 2:
        return scnd
    else:
        for i in range(2,n):
            nth = frst + scnd
            frst = scnd
            scnd = nth
        return scnd
