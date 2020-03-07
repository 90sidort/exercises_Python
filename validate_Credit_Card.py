# Description: https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2
# My solution:
def validate(n):
    n = list(str(n))
    m = []
    for x in range(0,len(n)):
        m.append(int(n[x]))
        if len(n) % 2 == 0:
            if x % 2 == 0:
                m[x] = m[x] * 2
        else:
            if x % 2 != 0:
                m[x] = m[x] * 2
    for x in range(0, len(m)):
        if m[x] > 9:
            m[x] = m[x] - 9
    return True if sum(m) % 10 == 0 else False