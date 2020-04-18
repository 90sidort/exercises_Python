# Description: https://www.codewars.com/kata/514a024011ea4fb54200004b/python
# Short task summary:
# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

# My solution:
import re
def domain_name(url):
    if 'http' in url and 'www' not in url:
        return (re.search('//(.*)', url).group(1)).split('.')[0]
    elif 'www' in url: 
        return (re.search('www.(.*)', url).group(1)).split('.')[0]
    else:
        return url.split('.')[0]