# Description: https://www.codewars.com/kata/5aee86c5783bb432cd000018/python
# Short task summary:
##Welcome to the Codewars Bar!
##
##Codewars Bar recommends you drink 1 glass of water per standard drink so you're not hungover tomorrow morning.
##
##Your fellow coders have bought you several drinks tonight in the form of a string. Return a string suggesting how many glasses of water you should drink to not be hungover.
##Example parties:
##Input 0:
##
##"1 beer"
##Output 0:
##
##"1 glass of water"
##Explaination 0:
##
##You drank one standard drink
##Input 1:
##
##"1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"
##Output 1:
##
##"10 glasses of water"
##Explaination 1:
##
##You drank ten standard drinks

# My solution:
def hydrate(drink_string):
    glasses = str(sum([int(x) for x in drink_string if x.isdigit()]))
    return glasses + " glasses of water" if glasses != "1" else glasses + " glass of water"
