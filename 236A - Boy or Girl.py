name = input()

given_string = list(name[:len(name)])

output = []

for char in given_string:
    if char in output:
        pass
    else:
        output.append(char)

if len(output) % 2 != 0 :
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")