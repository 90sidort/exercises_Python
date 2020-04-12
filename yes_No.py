# Description: https://www.codewars.com/kata/573c84bf0addf9568d001299/python
# Short task summary:
##Write a code that receives an array of numbers or strings, goes one by one through it while taking one value out, leaving one value in, taking, leaving, and back again to the beginning until all values are out.
##It's like a circle of people who decide that every second person will leave it, until the last person is there. So if the last element of the array is taken, the first element that's still there, will stay.
##The code returns a new re-arranged array with the taken values by their order. The first value of the initial array is always taken.
# My solution:
def yes_no(arr):
    first_len = len(arr)
    new_arr = []
    previous = 'Y'
    while len(arr) > 0:
        ind = []
        for x in range(len(arr)): 
            if previous == 'Y':
                new_arr.append(arr[x])
                previous = 'N'
                ind.append(x)
            else:
                previous = 'Y'
        arr = [el for el in arr if arr.index(el) not in ind]
    return new_arr
