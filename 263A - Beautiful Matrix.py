A=[]
for i in range(5):
    A.append([int(i) for i in input().split()])

for x in range(len(A)):
    for z in range(len(A[x])):
        if A[x][z] == 1:
            n_row = x
            n_col = z
turns = 0

while (n_row != 2) or (n_col != 2):
    if n_row > 2:
        n_row -= 1
        turns += 1
        
    elif n_row < 2:
        n_row += 1
        turns += 1
       
    if n_col > 2:
        n_col-= 1
        turns += 1
        
    elif n_col< 2:
        n_col += 1
        turns += 1
        
print(turns)
