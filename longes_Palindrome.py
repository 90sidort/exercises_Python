# Description: https://www.codewars.com/kata/54bb6f887e5a80180900046b
# My solution:
def longest_palindrome (s):
    if s == '':
        return 0
    s = s.lower()
    results = []
    for i in range(len(s)):
        for j in range(0, i):
            chunk = s[j:i + 1]
            if chunk == chunk[::-1]:
                results.append(chunk)
    return 1 if len(results) == 0 else len(max(results, key=len))