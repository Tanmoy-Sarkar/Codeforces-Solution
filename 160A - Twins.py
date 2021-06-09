n=int(input())
coins = input().split()
coins = [int(i) for i in coins]
coins.sort(reverse=True)
total = 0
no = 0
for i in range(n):
    no += 1
    total += coins[i]
    if total>sum(coins[i+1:]):
        break
print(no)


