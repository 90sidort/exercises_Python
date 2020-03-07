# Description: https://www.codewars.com/kata/583203e6eb35d7980400002a
# My solution:
def count_smileys(arr):
    valid_faces = [':D', ';~D', ':~)', ':)', ';D', ':~D', ';-D', ':-D']
    counter = 0
    for x in arr:
        if x in valid_faces:
            counter += 1
    return counter