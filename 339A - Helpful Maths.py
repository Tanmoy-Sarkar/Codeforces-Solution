sum_string = input()

sum_string = [int(num) for (num) in sum_string.split("+")]

turn = 0
output = ""
for num in sorted(sum_string):
    turn += 1
    if turn == len(sum_string):
        output += str(num)
    else:
        output += str(num)+"+"

print(output)
