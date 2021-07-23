import collections
n = int(input())
for _ in range(n):
    given = input()
    results = collections.Counter(given)
    output = 0

    status = False
    for i in results.values():
        if i > 1:
            output += 1
        elif status == True:
            output += 1
            status = False
        elif i == 1:
            status = True

    print(output)