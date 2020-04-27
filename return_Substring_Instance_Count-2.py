# Description: https://www.codewars.com/kata/52190daefe9c702a460003dd/python
# Short task summary:

##Complete the solution so that it returns the number of times the search_text is found within the full_text.
##
##search_substr( fullText, searchText, allowOverlap = true )
##
##so that overlapping solutions are (not) counted. If the searchText is empty, it should return 0. Usage examples:
##
##search_substr('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
##search_substr('aaabbbcccc', 'bbb') # should return 1
##search_substr( 'aaa', 'aa' ) # should return 2
##search_substr( 'aaa', '' ) # should return 0
##search_substr( 'aaa', 'aa', false ) # should return 1

# My solution:
def search_substr(full_text, search_text, allow_overlap=True):
    if allow_overlap == False and search_text != '':
        return full_text.count(search_text)
    elif allow_overlap == True and search_text != '':
        return len([1 for i in range(len(full_text)) if search_text in full_text[i:i+len(search_text)]])
    return 0
