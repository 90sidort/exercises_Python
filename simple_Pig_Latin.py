# Description: https://www.codewars.com/kata/520b9d2ad5c005041100000f
# My solution:
def pig_it(text):
    text = text.split()
    final_text = []
    for x in text:
        if x[0].isalpha() == True:
            x = list(x)
            x.append(x[0]+'ay')
            del x[0]
            final_x = "".join(x)
            final_text.append(final_x)
        else:
            final_text.append(x)
    return " ".join(final_text)