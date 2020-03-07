# Description: https://www.codewars.com/kata/55c6126177c9441a570000cc
# My solution:
def order_weight(strng):
    nrml_wght = strng.split()
    wght_wght = []
    for x in nrml_wght:
        d_sum = 0
        for d in str(x):
            d_sum += int(d)
        wght_wght.append(d_sum)
    wght_pairs = zip(wght_wght, nrml_wght)
    reordered = [x for _, x in sorted(wght_pairs)]
    return " ".join(reordered)