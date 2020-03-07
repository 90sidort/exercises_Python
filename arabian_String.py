# Description: https://www.codewars.com/kata/525821ce8e7b0d240b002615
# My solution:
def camelize(str_):
    new_str = ''
    last = True
    for x in str_:
        if (x.isalpha() or x.isdigit()) and last == False:
            new_str += x.lower()
        elif (x.isalpha() or x.isdigit()) and last == True:
            new_str += x.upper()
            last = False
        else:
            last =True
    return new_str