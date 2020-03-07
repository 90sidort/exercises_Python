# Description: https://www.codewars.com/kata/5a7893ef0025e9eb50000013
# My solution:
def max_gap(numbers):
    numbers = sorted(numbers)
    gap = 0
    for x in range(0, len(numbers) - 1):
        current_gap = numbers[x+1] - numbers[x]
        if current_gap < 0:
            current_gap = current_gap * (-1)
        if current_gap > gap:
            gap = current_gap
    return gap