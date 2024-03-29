from collections import deque
import sys
input = sys.stdin.readline


s = input().strip()
stack = deque()
count = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        if s[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)

