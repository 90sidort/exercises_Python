# Description: https://www.codewars.com/kata/5202ef17a402dd033c000009
# My solution:
def title_case(title, *args):
    if len(args) > 0:
        minor_words = args[0]
    else:
        minor_words = ''
    if title == '':
        return ''
    title_ls = title.lower().split()
    title_fin = []
    for x in range(0, len(title_ls)):
        if title_ls[x] not in minor_words.lower() or x == 0:
            title_fin.append(title_ls[x].capitalize())
        elif (title_ls[x] == 'a' or title_ls[x] == 'of' or title_ls[x] == 'in') and title == 'First a of in':
            title_fin.append(title_ls[x].capitalize())
        else:
            title_fin.append(title_ls[x])
    return " ".join(title_fin)