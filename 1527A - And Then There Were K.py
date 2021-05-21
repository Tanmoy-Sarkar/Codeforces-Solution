#gives time exceed error
t = int(input())
for j in range(t):
    k = int(input())
    sum_ = k
    for i in range (1,k):
       
        sum_ = sum_ & (k-i)
            
        if sum_ == 0:
            print(k-i) 
            break
            
    
