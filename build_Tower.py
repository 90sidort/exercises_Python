# Description: https://www.codewars.com/kata/576757b1df89ecf5bd00073b
# My solution:
def tower_builder(n_floors):
    length = (2 * n_floors) - 1
    array = []
    star = '*'
    side = ' '
    for x in range(0, n_floors):
        if n_floors == 1:
            array.append(star)
        else:
            string = (length - len(star)) // 2
            end_string = (side * string) + star + (side * string)
            array.append(end_string)
            star = star +'**'
    return array