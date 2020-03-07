# Description: https://www.codewars.com/kata/52761ee4cffbc69732000738
# My solution:
def goodVsEvil(good, evil):
    good_list, evil_list = good.split(), evil.split()
    good_sum = 0
    evil_sum = 0
    for x in range(0, len(good_list)):
        if x == 0:
            a = 1
        elif x == 1:
            a = 2
        elif x == 2 or x == 3:
            a = 3
        elif x == 4:
            a = 4
        elif x == 5:
            a = 10
        good_sum = good_sum + int(good_list[x]) * a

    for y in range(0, len(evil_list)):
        if y == 0:
            b = 1
        elif y == 1 or y == 2 or y == 3:
            b = 2
        elif y == 4:
            b = 3
        elif y == 5:
            b = 5
        elif y == 6:
            b = 10
        evil_sum = evil_sum + int(evil_list[y]) * b

    if good_sum > evil_sum:
        return 'Battle Result: Good triumphs over Evil'
    elif good_sum == evil_sum:
        return 'Battle Result: No victor on this battle field'
    else:
        return 'Battle Result: Evil eradicates all trace of Good'