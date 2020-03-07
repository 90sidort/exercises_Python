# Description: https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
# My solution:
def validate_pin(pin):
    return (len(pin) in [4,6]) and (set([c in '1234567890' for c in pin]) == {True})
