n= input()

def check_lucky(n):
    n = [i for i in n]
    for i in n:
        if i != "4" and i != "7":
            return False
    return True

number = [i for i in n]

for x in range(1,int(n)+1):
    if int(n)%x==0 and check_lucky(str(x))==True:
        print("YES")
        break
else:
    print("NO")

