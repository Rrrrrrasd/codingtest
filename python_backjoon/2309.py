import sys
input = sys.stdin.readline


height_list = list()
for _ in range(9):
    height_list.append(int(input()))

height_list.sort()
sum = sum(height_list)

idx1 = 0
idx2 = 1
while idx1 != 7:
    if sum - (height_list[idx1] + height_list[idx2]) == 100:
        break
    if idx2 == 8:
        idx1 += 1
        idx2 = idx1
    idx2 += 1

height_list.pop(idx1)
height_list.pop(idx2-1)

for height in height_list:
    print(height, end=' ')


