# Description: https://www.codewars.com/kata/51646de80fd67f442c000013
# Short task summary:

# Complete the method so that it does the following:

#     Removes any duplicate query string parameters from the url (the first occurence should be kept)
#     Removes any query string parameters specified within the 2nd argument (optional array)

# Examples:

# strip_url_params('www.codewars.com?a=1&b=2&a=2') == 'www.codewars.com?a=1&b=2'
# strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b']) == 'www.codewars.com?a=1'
# strip_url_params('www.codewars.com', ['b']) == 'www.codewars.com'

# My solution:
def strip_url_params(url, params_to_strip=[]):
    crrnt_prmtrs = []
    if '?' not in url:
        return url
    else:
        link, prmtrs = url.split('?')[0], url.split('?')[1].split('&')
        chckd_prmtrs = []
        new_prmtrs = ''
        for i in range(len(prmtrs)):
            if prmtrs[i][0] not in chckd_prmtrs and prmtrs[i][0] not in params_to_strip:
                chckd_prmtrs.append(prmtrs[i][0])
                if i == 0:
                    new_prmtrs += ('?' + prmtrs[i] + '&')
                else:
                    new_prmtrs += (prmtrs[i] + '&')
        result = link + new_prmtrs 
        return result if result[-1] != '&' else result[0:-1]