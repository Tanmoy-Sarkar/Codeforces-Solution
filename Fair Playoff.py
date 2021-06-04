n = int(input())

for _ in range(n):
    given = input().split(' ')
    skills = [int(i) for i in given]
    result1 = max(skills[:2])
    result2 = max(skills[2:])
    if result1 and result2 in sorted(skills,reverse=True)[:2]:
        print("YES")
    else:
        print("NO")
    

