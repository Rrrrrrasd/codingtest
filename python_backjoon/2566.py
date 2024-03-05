n, m = 9, 9

procession = []
max_val = 0
max_val_idx = [0, 0]


for _ in range(n):
    temp = list(map(int, input().split()))
    procession.append(temp)


for i in range(n):
    for j in range(m):
        if procession[i][j] > max_val:
            max_val = procession[i][j]
            max_val_idx[0] = i
            max_val_idx[1] = j

print(max_val)
print(max_val_idx[0]+1, max_val_idx[1]+1)
