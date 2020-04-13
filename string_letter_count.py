# Description: https://www.codewars.com/kata/59e19a747905df23cb000024
# Short task summary:
##Take a string str and return a string that is made up of the number of occurances of each english letter in str, followed by that letter. The string shouldn't contain zeros; leave them out.
##
##An empty string, or one with no letters, should return an empty string.
##Notes
##
##    Ignore all case
##    str will never be null
##
# My solution:
import string
def string_letter_count(s):
    return "".join([str(s.lower().count(x)) + x for x in string.ascii_lowercase if x in s.lower()])
