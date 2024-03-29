from collections import deque
import sys
input = sys.stdin.readline


n = int(input())

line_now = deque(map(int, input().strip().split()))
stack = deque()

target = 1
for human in line_now:
    stack.append(human)

    while stack and stack[-1]==target:
        stack.pop()
        target+=1

if stack:
    print('Sad')
else:
    print('Nice')
