n,k=input().split()  
n,k = int(n),int(k)
scores_input = input().split()
scores = [int(i) for i in scores_input]
cut_off = scores[k-1]

count=0
for i in scores:
    
    if i>=cut_off and i>0: 
        count += 1
    else:
        break
    
print(count)