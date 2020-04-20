# Description: https://www.codewars.com/kata/522551eee9abb932420004a0
# Short task summary:

# I love Fibonacci numbers in general, but I must admit I love some more than others.

# I would like for you to write me a function that when given a number (n) returns the n-th number in the Fibonacci Sequence.

# For example:

#    nth_fib(4) == 2

# Because 2 is the 4th number in the Fibonacci Sequence.

# For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.


# My solution:
def nth_fib(n):
    frst, scnd = 0, 1
    for i in range(n-1):
        frst, scnd = scnd, frst + scnd
    return frst
