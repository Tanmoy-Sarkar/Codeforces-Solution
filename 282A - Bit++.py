n=int(input())
output = 0
for i in range(n):
    statement = input()
    x= statement.split("X")

    if "++" in x:
        output += 1
    else:
        output -= 1

print(output)