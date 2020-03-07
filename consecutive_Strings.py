# Description: https://www.codewars.com/kata/56a5d994ac971f1ac500003e
# My solution:
def longest_consec(strarr, k):
    if len(strarr) == 0 or k <= 0 or k > len(strarr):
        return ""
    longest = ''
    for i in range(0, len(strarr)):
        current = strarr[i:i+k]
        if len("".join(current)) > len("".join(longest)):
            longest = current
    return "".join(longest)