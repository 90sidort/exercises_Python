# Description: https://www.codewars.com/kata/54a0689443ab7271a90000c6
# My solution:
import sys
class Harshad:
    def is_valid(number):
        num = list(str(number))
        sums = 0
        for x in num:
            sums = sums + int(x)
        return True if number % sums == 0 else False
    def get_next(number):
        while True:
            number += 1
            if Harshad.is_valid(number) == True:
                return number
    def get_series(count, start=0):
        resp = []
        for x in range(start+1, sys.maxsize**10):
            if Harshad.is_valid(x) == True:
                resp.append(x)
            if len(resp) == count:
                return resp