cost,total_money,no = input().split()

cost,total_money,no = int(cost),int(total_money),int(no)

needed_money = 0

for i in range(1,no+1):
    needed_money += i*cost

if needed_money > total_money:
    print(needed_money-total_money)

else:
    print(0)