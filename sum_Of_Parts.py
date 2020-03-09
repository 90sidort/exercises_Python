# Description: https://www.codewars.com/kata/5ce399e0047a45001c853c2b
# My solution:
def parts_sums(ls):
    first_sum = sum(ls)
    summary_list = [first_sum]
    for x in ls:
        first_sum = first_sum - x
        summary_list.append(first_sum)
    return summary_list