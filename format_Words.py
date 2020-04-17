# Description: https://www.codewars.com/kata/51689e27fe9a00b126000004/python
# Short task summary:
##Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single formatted string. Empty string values should be ignored. Empty arrays or null/nil values being passed into the method should result in an empty string being returned. 

# My solution:
def format_words(words):
    if words == None:
        return ""
    words = [w for w in words if w != '']
    if len(words) == 0:
        return ""
    elif len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return words[0] + ' and ' + words[1]
    else:
        first = ", ".join([word for word in words[:-1]])
        return first + " and " + words[-1]
