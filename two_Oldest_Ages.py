# Description: https://www.codewars.com/kata/511f11d355fe575d2c000001
# My solution:
def two_oldest_ages(ages):
    ages = sorted(ages)
    return [ages[-2], ages[-1]]