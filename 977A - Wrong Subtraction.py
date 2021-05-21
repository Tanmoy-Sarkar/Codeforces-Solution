n,k = input().split()


for i in range(int(k)):
    if int(n[-1]) != 0:
        n = str(int(n)-1)
    else:
        n = str(int(int(n)/10))

print(n)