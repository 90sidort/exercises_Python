# Description: https://www.codewars.com/kata/5a53a17bfd56cb9c14000003
# My solution:
def disarium_number(number):
    check = number
    number = list(str(number))
    sum_sum = 0
    for x in range(0,len(number)):
        sum_sum = sum_sum + (int(number[x]) ** (x+1))
    return 'Disarium !!' if sum_sum == check else 'Not !!'