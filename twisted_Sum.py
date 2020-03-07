# Description: https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f
# My solution:
def compute_sum(n):
    n_listed = []
    for d in range (1, n+1):
        if len(str(d)) > 1:
            for i in list(str(d)):
                n_listed.append(int(i))
        else:
            n_listed.append(int(d))
    return sum(n_listed)