def insr():
    s = input()
    return(list(s[:len(s)]))

s = insr()
vowels = ['a','e','i','o','u','y']
for letter in range(len(s)):
    
    if s[letter].isupper():
        s[letter] = s[letter].lower()

temp_string=[]
for letter in s:
    
    if letter in vowels:
        pass
    else:
        temp_string.append(letter)
s = temp_string
temp_string = []
for letter in s:
    temp_string.extend(['.',letter])
    
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # return string  
    return (str1.join(s))

print(listToString(temp_string))