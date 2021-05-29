n = int(input())
capacity = []
status = 0
for i in range(n):
    exit,enter = input().split()
    exit,enter = int(exit),int(enter)
    status=status+enter-exit
    capacity.append(status)

print(max(capacity))
