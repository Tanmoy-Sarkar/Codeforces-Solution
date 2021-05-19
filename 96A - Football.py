players = input()

players= list(players[:len(players)])
flag = False


for i in range(len(players)):
    if len(players)<=7:
        print("NO")
        flag = True
        break
    elif players[i:i+7].count(players[i]) == 7 :
        print("YES")
        flag = True
        break

if flag == False:
    print("NO")

