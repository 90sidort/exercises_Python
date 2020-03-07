# Description: https://www.codewars.com/kata/5583d268479559400d000064
# My solution:
def binary_to_string(binary):
    if binary == '':
        return ''
    binary_list = [binary[i:i+8] for i in range(0, len(binary), 8)]
    decimal_list = []
    for x in binary_list:
        i = 8
        sums = 0
        for y in x:
            sums = sums + (int(y) * 2**(i-1))
            i -= 1
        decimal_list.append(sums)
    char_list = [chr(x) for x in decimal_list]
    return "".join(char_list)