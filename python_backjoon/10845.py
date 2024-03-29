import sys
from collections import deque

input = sys.stdin.readline

def order_play(queue:deque, command_order:list):
    command = command_order[0]
    if command == 'push':
        x = command_order[1]
        queue.append(x)
    
    if command == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    if command == 'size':
        print(len(queue))

    if command == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    if command =='front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    if command =='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    




n = int(input())
queue = deque()

for _ in range(n):
    command_order= list(input().split())
    order_play(queue, command_order)
