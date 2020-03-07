# Description: https://www.codewars.com/kata/59daf400beec9780a9000045
# My solution:
def name_in_str(string, name):
    index = 0
    for x in name.lower():
        string = string[index:].lower()
        if x not in string:
            return False
        else:
            index = string.index(x) + 1
    return True