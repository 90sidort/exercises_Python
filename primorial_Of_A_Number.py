# Description: https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124
# My solution:
from functools import reduce
def num_primorial(N):
    n_primes = []
    i, j, flag = 0, 0, 0
    for i in range(1, 7920, 1):
        if len(n_primes) < N:
            if (i == 1 or i == 0):
                continue
            flag = 1
            for j in range(2, ((i // 2) + 1), 1):
                if (i % j == 0):
                    flag = 0
                    break
            if (flag == 1):
                n_primes.append(i)
        else:
            break
    return reduce(lambda x, y: x*y, n_primes)