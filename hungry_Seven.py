# Description: https://www.codewars.com/kata/59e61c577905df540000016b
# Short task summary:
##Seven is a hungry number and its favourite food is number 9. Whenever it spots 9 through the hoops of 8, it eats it! Well, not anymore, because you are going to help the 9 by locating that particular sequence (7,8,9) in an array of digits and tell 7 to come after 9 instead. Seven "ate" nine, no more! (If 9 is not in danger, just return the same array)
# My solution:
def hungry_seven(arr):
    change = True
    i = 0
    while True:
        start = i
        for x in range(len(arr)):
            if arr[x:x+3] == [7,8,9]:
                arr[x:x+3] = [8,9,7]
                i += 1
        if start == i:
            break
    return arr
