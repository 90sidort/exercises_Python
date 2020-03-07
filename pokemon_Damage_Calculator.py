# Description: https://www.codewars.com/kata/536e9a7973130a06eb000e9f
# My solution:
def calculate_damage(your_type, opponent_type, attack, defense):
    print(your_type, opponent_type, attack, defense)
    if your_type == 'fire':
        if opponent_type == 'fire':
            effect = 0.5
        elif opponent_type == 'grass':
            effect = 2
        elif opponent_type == 'water':
            effect = 0.5
        else:
            effect = 1
    elif your_type == 'water':
        if opponent_type == 'grass':
            effect = 0.5
        elif opponent_type == 'electric':
            effect = 0.5
        elif opponent_type == 'water':
            effect = 0.5
        else:
            effect = 2
    elif your_type == 'electric':
        if opponent_type == 'grass':
            effect = 1
        elif opponent_type == 'electric':
            effect = 0.5
        elif opponent_type == 'water':
            effect = 2
        else:
            effect = 1
    else:
        if opponent_type == 'grass':
            effect = 0.5
        elif opponent_type == 'electric':
            effect = 1
        elif opponent_type == 'water':
            effect = 2
        else:
            effect = 0.5
    return 50 * ( attack/ defense) * effect