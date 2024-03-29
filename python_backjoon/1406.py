from collections import deque
import sys
input = sys.stdin.readline

def command_play(s1:deque, s2:deque, command_order:list):
    command = command_order[0]
    if command =='L':
        if s1:
            s2.append(s1.pop())
    
    if command =='D':
        if s2:
            s1.append(s2.pop())

    if command =='B':
        if s1:
            s1.pop()
    
    if command =='P':
        x = command_order[1]
        s1.append(x)



s1 = deque(input().strip())
s2 = deque()

n = int(input())

for _ in range(n):
    command_order = list(input().split())
    command_play(s1, s2, command_order)

print(''.join(s1)+''.join(reversed(s2)))
