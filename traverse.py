import os
import re
from glob import glob

# Used glob module to recursively search for txt files in a directory
result = [y for x in os.walk(".") for y in glob(os.path.join(x[0], '*.txt'))]

phone_numbers = []
regex_str_phone = "[0-9]{1,3}(\-|\ )\([0-9]{3}\)[0-9]{3}(\-|\ )[0-9]{4}$"         # xx-(xxx)xxx-xxxx
regex_str_US = "\+[0-9]{1,3}(\-|\ )\([0-9]{3}\)(\-|\ )[0-9]{3}(\-|\ )[0-9]{4}$"   # +xx-(xxx)-xxx-xxxx
regex_str_IND_1 = "\+[0-9]{2}(\-|\ )[0-9]{4}(\-|\ )[0-9]{6}$"                     # +xx-xxxx-xxxxxx
regex_str_IND_2 = "\+[0-9]{2}(\-|\ )[0-9]{3}(\-|\ )[0-9]{7}$"                     # +xx-xxx-xxxxxxx
regex_str_IND_3 = "\+[0-9]{2}(\-|\ )[0-9]{2}(\-|\ )[0-9]{8}$"                     # +xx-xx-xxxxxxxx
regex_str_IND_mobile = "[0-9]{10}$"                                               # xxxxxxxxxx
regex_str_IND_landline = "[0-9]{3}(\-|\ )[0-9]{8}"                                # xxx-xxxxxxxx
regex_str_others = "^\+[1-9]{1}[0-9]{3,14}$"

pattern_1 = re.compile(regex_str_phone)
pattern_2 = re.compile(regex_str_US)
pattern_3 = re.compile(regex_str_IND_1)
pattern_4 = re.compile(regex_str_IND_mobile)
pattern_5 = re.compile(regex_str_others)
pattern_6 = re.compile(regex_str_IND_landline)
pattern_7 = re.compile(regex_str_IND_2)
pattern_8 = re.compile(regex_str_IND_3)

# Case1: when data is structured and separated by comma's
# Case2: when data is unstructured
        #sub-case1: when data is structured but phone number can be anywhere
        #sub-case2: when there is some garbage data

for files in result:
    file = open(files , 'r')
    for lines in file:
        curr_line = lines.split(',')

        for p in curr_line:
            if pattern_1.match(p) or pattern_2.match(p) or pattern_3.match(p) or pattern_4.match(p) or pattern_5.match(p) or pattern_6.match(p) or pattern_7.match(p) or pattern_8.match(p):
                phone_numbers.append(p)


print (phone_numbers)
