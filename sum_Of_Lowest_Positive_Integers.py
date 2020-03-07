# Description: https://www.codewars.com/kata/558fc85d8fd1938afb000014
# My solution:
def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    return numbers[0] + numbers[1]