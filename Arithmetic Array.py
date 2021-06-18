n = int(input())

for _ in range(n):
    length = int(input())
    arr = [int(i) for i in input().split()]
    total = sum(arr)
    if total == length:
        print("0")
    elif length>total:
        print("1")
    else:
        print(total-length)
