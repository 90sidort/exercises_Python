# Description: https://www.codewars.com/kata/58223370aef9fc03fd000071
# My solution:
def dashatize(num):
    if num == None:
        return "None"
    else:
        return ''.join(['-'+d+'-' if int(d)%2 else d for d in str(abs(num))]).replace('--','-').strip('-')