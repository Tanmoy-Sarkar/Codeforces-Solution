n = input()
given = [i for i in n]
total = given.count("4") + given.count("7")
if total == 4 or total == 7:
    print("YES")
else:
    print("NO")