# Description: https://www.codewars.com/kata/56c0ca8c6d88fdb61b000f06
# My solution:
def next_version(version):
    version = version.split('.')
    changed = False
    for d in range(len(version)-1, -1,-1):
        if version[d] == '9' and changed == False and d != 0:
            version[d] = '0'
        elif version[d] == '9' and changed == False and d == 0:
            version[d] = '10'
        elif version[d] != '9' and changed == False:
            version[d] = str(int(version[d]) + 1)
            changed = True
    return '.'.join(version)
