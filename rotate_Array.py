# Description: https://www.codewars.com/kata/54f8b0c7a58bce9db6000dc4
# My solution:
def rotate(arr, n):
    minus = False if n > 0 else True
    n = n if n > 0 else n * (-1)
    while n > 0:
        if minus == False:
            temp_arr = arr[:len(arr) - 1]
            temp_arr.insert(0, arr[len(arr) - 1])
        else:
            temp_arr = arr[1:]
            temp_arr.insert(len(arr) - 1, arr[0])
        n -= 1
        arr = temp_arr
    return arr
