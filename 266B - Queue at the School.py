n,time = input().split()
n,time = int(n),int(time)

standings = [i for i in input()]

for s in range(time):
    i=0
    while i < len(standings)-1:
        
        if standings[i] == "B" and standings[i+1] == "G" :
            standings[i+1],standings[i] = "B","G"
            i += 2
        else:
            i += 1
            
print("".join(standings))