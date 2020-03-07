# Description: https://www.codewars.com/kata/52b757663a95b11b3d00062d
# My solution:
def to_weird_case(string):
    string = string.split()
    new_string = ''
    for y in string:
        new_string = new_string + ' '
        for x in range(0, len(y)):
            if x % 2 != 0:
                new_string = new_string + y[x].lower()
            else:
                new_string = new_string + y[x].upper()

    return new_string.strip()