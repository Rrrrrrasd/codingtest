from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

temp_list = list(map(int, input().strip().split()))
deq = deque()

for i in range(n):
    deq.append((i+1, temp_list[i]))


idx_count = 1
result = list()
while len(deq):
    idx, val = deq.popleft()
    print(idx, end=' ')
    if val > 0:
        deq.rotate(-(val-1))
    else:
        deq.rotate(-val)








