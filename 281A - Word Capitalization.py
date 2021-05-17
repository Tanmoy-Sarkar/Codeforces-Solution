given_string = input()

given_string = list(given_string[:len(given_string)])

given_string[0] = given_string[0].upper()
output = ''.join([str(elem) for elem in given_string])
  
print(output)