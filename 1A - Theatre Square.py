import math
n,m,a=input().split()  
n,m,a=int(n),int(m),int(a) 


total = math.ceil(n/a)* math.ceil(m/a)

print(total)