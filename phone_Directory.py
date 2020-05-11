# Description: https://www.codewars.com/kata/56baeae7022c16dd7400086e
# Short task summary:

##John keeps a backup of his old personal phone book as a text file. On each line of the file he can find the phone number (formated as +X-abc-def-ghij where X stands for one or two digits), the corresponding name between < and > and the address.
##
##Unfortunately everything is mixed, things are not always in the same order; parts of lines are cluttered with non-alpha-numeric characters (except inside phone number and name).
##
##Examples of John's phone book lines:
##
##"/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"
##
##" 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
##
##"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"
##
##Could you help John with a program that, given the lines of his phone book and a phone number num returns a string for this number : "Phone => num, Name => name, Address => adress"
##
##Examples:
##
##s = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
##
##phone(s, "1-541-754-3010") should return "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
##
##It can happen that there are many people for a phone number num, then
##
##return : "Error => Too many people: num"
##
##or it can happen that the number num is not in the phone book, in that case
##
##return: "Error => Not found: num"
##
##You can see other examples in the test cases.

# My solution:
import re
forbade = '/$*?,;:'
def phone(strng, num):
    dr_list = [x for x in strng.split("\n") if len(x) > 1]
    record = [r for r in dr_list if num in r]
    if len(record) > 1:
        return "Error => Too many people: {}".format(num)
    elif len(record) == 0:
        return "Error => Not found: {}".format(num)
    else:
        record = record[0]
    name = (re.compile("\<.*\>").search(record)).group(0)
    number = (re.compile("\+\d*\-*\d*\-*\d*\-*\d*").search(record)).group(0)
    start_name, end_name, start_number, end_number = record.find(name), record.find(name) + len(name), record.find(number), record.find(number) + len(number)
    range_name, range_number = range(start_name, end_name+1), range(start_number, end_number+1)
    address = ("").join([record[i] for i in range(len(record)) if i not in range_name and i not in range_number and record[i] not in forbade])
    return_name = name[1:-1].strip()
    return_number = ("".join([x for x in number if x.isdigit() or x == '-'])).strip()
    return_address = " ".join([x for x in address.split() if ' ' not in x]).strip()
    return_address = (return_address.replace('_', ' ')).strip()
    return "Phone => {}, Name => {}, Address => {}".format(return_number, return_name, return_address)
