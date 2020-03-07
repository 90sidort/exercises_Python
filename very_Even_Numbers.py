# Description: https://www.codewars.com/kata/58c9322bedb4235468000019
# My solution:
def is_very_even_number(n):
    n_list = list(str(n))
    while len(n_list) > 1:
        suma = 0
        for x in n_list:
            suma = suma + int(x)
        n_list = list(str(suma))
    if int(n_list[0]) % 2 == 0:
        return True
    else:
        return False