lim_weight,bob_weight = input().split()
lim_weight,bob_weight = int(lim_weight),int(bob_weight)
years = 1
while True:
    lim_weight *= 3
    bob_weight *= 2
    if lim_weight > bob_weight :
        break
    years += 1

print(years)