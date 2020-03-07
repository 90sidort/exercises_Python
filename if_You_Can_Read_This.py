# Description: https://www.codewars.com/kata/586538146b56991861000293
# My solution:
import string
nato_dict = {'a':'Alfa', 'b':'Bravo', 'c':'Charlie', 'd':'Delta', 'e':'Echo', 'f':'Foxtrot',
'g':'Golf', 'h':'Hotel', 'i':'India', 'j':'Juliett', 'k':'Kilo', 'l':'Lima', 'm':'Mike',
'n':'November', 'o':'Oscar', 'p':'Papa','q':'Quebec', 'r':'Romeo', 's':'Sierra','t':'Tango',
'u':'Uniform', 'v':'Victor', 'w':'Whiskey', 'x':'Xray', 'y':'Yankee', 'z':'Zulu'}
def to_nato(words):
    nato_words = []
    for x in words:
        if x in string.ascii_letters:
            nato_words.append(nato_dict[x.lower()])
        elif x in '!,.?':
            nato_words.append(x)
    return " ".join(nato_words)