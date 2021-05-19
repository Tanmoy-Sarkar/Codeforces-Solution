mat = []
n = input()
for i in range(int(n)):

    a,b,c = input().split()
    mat.append([int(a),int(b),int(c)])
flag = 0

for j in range(3):
    total = 0
    for i in range(int(n)):
        total += mat[i][j]
    if total == 0:
        flag += 1
if flag == 3:
    print("YES")
else:
    print("NO")