# Description: https://www.codewars.com/kata/59cfc000aeb2844d16000075/python
# Short task summary:

# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.
# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
# The input will be a lowercase string with no spaces.
# Good luck!

# My solution:
def capitalize(s):
    return ["".join([s[n].upper() if n % 2 == 0 else s[n] for n in range(0,len(s))]), "".join([s[n].upper() if n % 2 != 0 else s[n] for n in range(0,len(s))])]
