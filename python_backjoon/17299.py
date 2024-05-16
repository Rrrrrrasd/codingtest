import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
num_list = list(map(int, input().strip().split()))
num_dict = dict()

for num in num_list:
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

answer = [-1]*n
stack = deque()

stack.append(0)
for i in range(1,n):
    while stack and num_dict[num_list[stack[-1]]] < num_dict[num_list[i]]:
        answer[stack.pop()] = num_list[i]
    stack.append(i)

print(*answer)