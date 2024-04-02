import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
A = list(map(int, input().split()))
answer = [-1] * n
stack = deque()

stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)
    

print(*answer)
