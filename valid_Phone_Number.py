# Description: https://www.codewars.com/kata/525f47c79f2f25a4db000025
# My solution:
def validPhoneNumber(phoneNumber):
    if phoneNumber[0] != '(' or phoneNumber[4] != ')' or phoneNumber[5] != ' ':
        return False
    if phoneNumber[1:4].isdigit() != True:
        return False
    if phoneNumber[6:9].isdigit() != True:
        return False
    if phoneNumber[9] != '-':
        return False
    if phoneNumber[10:14].isdigit() != True:
        return False
    if len(phoneNumber) != 14:
        return False
    return True