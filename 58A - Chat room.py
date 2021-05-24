import re
given_string = input()


try:
    result = (re.search('h(.*)o', given_string)).group(1)
else:
    pass
try:
    result2 = (re.search('e(.*)l', result)).group(1)
else:
print(result2)