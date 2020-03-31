# Description: https://www.codewars.com/kata/56bdd0aec5dc03d7780010a5/python
# Short task summary:

##Your task is to Find the next higher number (int) with same '1'- Bits.
##
##I.e. as much '1' bits as before and output next higher than input. Input is always an int >0 up to 1<<30. No bad cases or special tricks... 


# My solution:
def next_higher(value):
    strt = (bin(value).replace("0b", "")).count('1')
    while True:
        value += 1
        if strt == (bin(value).replace("0b", "")).count('1'):
            return value
