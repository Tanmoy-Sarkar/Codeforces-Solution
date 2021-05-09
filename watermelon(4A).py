w= int(input())

for i in range(1,w):
    part1 = w-i
    part2 = i
    if part1%2==0 and part2%2==0:
        print("YES")
        break
else:
    print("NO")
        


