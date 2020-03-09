# Description: https://www.codewars.com/kata/554ca54ffa7d91b236000023
# My solution:
def delete_nth(order,max_e):
    ordered = []
    for x in order:
        if ordered.count(x) < max_e:
            ordered.append(x)
    return ordered