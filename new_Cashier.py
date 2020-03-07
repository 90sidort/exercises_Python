# Description: https://www.codewars.com/kata/5d23d89906f92a00267bb83d
# My solution:
def get_order(order):
    items = ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke']
    end_string = ''
    for x in items:
        if order.count(x.lower()) > 0:
            end_string += (x + ' ') * order.count(x.lower())
    return end_string.strip()