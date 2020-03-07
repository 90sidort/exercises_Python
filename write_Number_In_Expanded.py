# Description: https://www.codewars.com/kata/5842df8ccbd22792a4000245
# My solution:
def expanded_form(num):
    num = list(str(num))
    new_num = ''
    d = len(num)
    for x in num:
        if int(x) != 0:
            x = int(x) * (10 ** (d-1))
            new_num = new_num + str(x) + ' + '
        d -= 1
    return new_num[:-3]