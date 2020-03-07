# Description: https://www.codewars.com/kata/5e4217e476126b000170489b
# My solution:
def polydivisible(x):
    curr_num = ''
    x = list(str(x))
    for d in range(0,len(x)):
        curr_num += x[d]
        if int(curr_num) % (d+1) != 0:
            return False
    return True