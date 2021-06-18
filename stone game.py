a=[2,1,3,4,5,6,8,7]

high = max(a)
low = min(a)
low_i = 0
high_i = len(a)-1
steps = 0
high_index = a.index(high)
low_index = a.index(low)
if high_index>low_index:
    dis_low = low_index - low_i
    dis_high = high_i - high_index
else:
    dis_low = high_i - low_index
    dis_high = high_index - low_i

if dis_high>dis_low:
    print("YES")
    low_i = dis_low + 1
    steps += dis_low + 1
    dis_high1 = high_i - high_index
    dis_high2 = high_index - low_i
    if dis_high1>dis_high2:
        steps += dis_high2 + 1
    else:
        steps += dis_high1 +1
else:
    high_i = dis_high - 1
    steps += dis_high + 1
    dis_low1 = low_index - low_i
    dis_low2 = high_i - low_index
    if dis_low1>dis_low2:
        steps += dis_low2 + 1
    else:
        steps += dis_low1 + 1

    print("NO")
    
print(steps)