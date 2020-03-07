# Description: https://www.codewars.com/kata/5cde4e3f52910d00130dc92c
# My solution:
import re
def men_still_standing(cards):
    a, b = 11, 11
    ya, yb, ra, rb = [], [], [], []
    for card in cards:
        number = "".join(re.findall(r'\d+', card))
        if a >= 7 and b >= 7:
            if (card[0] == 'A') and (card[-1] == 'Y') and (ya.count(number) <=1) and (number not in ra):
                ya.append(number)
                if (ya.count(number) == 2):
                    a -= 1
            elif (card[0] == 'B') and (card[-1] == 'Y') and (yb.count(number) <=1) and (number not in rb):
                yb.append(number)
                if (yb.count(number) == 2):
                    b -= 1
            elif (card[0] == 'A') and (card[-1] == 'R') and (ra.count(number) <=0) and (ya.count(number) <= 1):
                ra.append(number)
                if (ra.count(number) == 1):
                    a -= 1
            elif (card[0] == 'B') and (card[-1] == 'R') and (rb.count(number) <=0) and (yb.count(number) <= 1):
                rb.append(number)
                if (rb.count(number) == 1):
                    b -= 1
    return (a,b)