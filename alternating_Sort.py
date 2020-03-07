# Description: https://www.codewars.com/kata/5ac49156376b11767f00060c
# My solution:
def alternate_sort(l):
    ans = []
    last_odd = 0
    l = sorted(l, key=abs)
    even = [e for e in l if e >= 0]
    odd = [o for o in l if o < 0]
    if odd:
        for num in range(len(odd)):
            last_odd += 1
            ans.append(odd[num])
            if num < len(even):
                ans.append(even[num])
    if last_odd-1 < len(even):
        ans += even[last_odd:]
    return ans