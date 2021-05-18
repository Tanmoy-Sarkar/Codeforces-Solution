n= input()
given_string = input()

given_string = list(given_string[:len(given_string)])
turn = 0
i=0

while i < (len(given_string)-1):
    if given_string[i] == given_string[i+1]:
        given_string.pop(i+1)
        turn += 1
    else:
        i += 1

print(turn)