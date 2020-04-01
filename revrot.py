# Description: https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991
# Short task summary:

##The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).
##
##If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.
##
##If
##
##    sz is <= 0 or if str is empty return ""
##    sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".


# My solution:
def revrot(strng, sz):
    if sz == 0:
        return ""
    lst = []
    for i in range(0,len(strng), sz):
        lst.append(strng[i:i+sz]) if len(strng[i:i+sz]) == sz else None
    final_lst = []
    for x in lst:
        digs_sum = 0
        for d in x:
            dig_sum = int(d) ** 2
            digs_sum += dig_sum
        if digs_sum % 2 == 0:
            final_lst.append(x[::-1])
        else:
            final_lst.append(x[1:] + x[0])
    return "".join(final_lst)
