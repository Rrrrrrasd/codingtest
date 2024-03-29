import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
stack = deque()

for _ in range(n):
    vps = input().strip()
    stack.clear()
    
    for p in vps:
        if p == '(':
            stack.append(p)
        elif p ==')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
            



  