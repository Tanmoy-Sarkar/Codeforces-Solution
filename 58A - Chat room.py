import re
given_string = input()


try:
    result = (re.search('h(.*)o', given_string)).group(1)
    result2 = (re.search('e(.*)l', result)).group(1)
    if "l" in result2:
        print("YES")
    else:
        print("NO")
    
except:
    print("NO")
    
