n=int(input())
total = 0
for i in range(n):

    views = input().split()
    if views.count("1")>=2 :
        total += 1

print(total)
