# Description: https://www.codewars.com/kata/56b861671d36bb0aa8000819
# My solution:
def reverse_and_combine_text(text):
    text = text.split()
    new_text = []
    while len(text) > 1:
        for x in text:
            x = x[::-1]
            new_text.append(x)
        text = []
        text = [x+y for x,y in zip(new_text[0::2], new_text[1::2])]
        odd = True if len(new_text) % 2 != 0 else False
        if odd:
            text.append(new_text[-1])
        new_text = []
    return "".join(text)