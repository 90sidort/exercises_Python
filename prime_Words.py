# Description: https://www.codewars.com/kata/5b1e2c04553292dacd00009e
# Short task summary:

##X and Y are playing a game. A list will be provided which contains n pairs of strings and integers. They have to add the integeri to the ASCII values of the stringi characters. Then they have to check if any of the new added numbers is prime or not. If for any character of the word the added number is prime then the word will be considered as prime word.
##
##Can you help X and Y to find the prime words?
##Example:
##
##prime_word([["Emma", 30], ["Liam", 30]])  ->  [1, 1]
##
##    For the first word "Emma" ASCII values are: 69 109 109 97
##    After adding 30 the values will be: 99 139 139 127
##    As 139 is prime number so "Emma" is a Prime Word.


# My solution:
def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

def prime_word(array):
    nswr = []
    for x in array:
        vls = [ord(char) + x[1] for char in x[0]]
        if any([isPrime(x) for x in vls]) == True:
            nswr.append(1)
        else:
            nswr.append(0)
    return nswr
