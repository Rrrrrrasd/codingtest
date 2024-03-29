from collections import deque
import sys
input = sys.stdin.readline

def order_queue(queue:deque, order_list:list):
    order = order_list[0]
    if len(order_list) == 2:
        x = int(order_list[1])
        queue.append(x)

    if order == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print('-1')
    
    if order == 'size':
        print(len(queue))
    
    if order == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    
    if order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    
    if order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)




n = int(input())
queue = deque()

for _ in range(n):
    order_list = list(map(str, input().split()))
    order_queue(queue, order_list)