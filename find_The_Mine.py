# Description: https://www.codewars.com/kata/528d9adf0e03778b9e00067e
# My solution:
def mineLocation(field):
    return list([(i, mine.index(1)) for i, mine in enumerate(field) if 1 in mine][0])