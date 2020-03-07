# Description: https://www.codewars.com/kata/554910d77a3582bbe300009c
# My solution:
def get_winner(ballots):
    highest_value = 0
    highest_name = ''
    votes = len(ballots)
    for x in set(ballots):
        if ballots.count(x) > highest_value:
            highest_value = ballots.count(x)
            highest_name = x
    if (highest_value * 100) / votes > 50:
        return highest_name
    else:
        None