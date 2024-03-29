from collections import deque
import sys
input = sys.stdin.readline

def command_function(deq:deque ,command, x=0):
    if command == 1:
        deq.appendleft(x)
    if command == 2:
        deq.append(x)
    if command == 3:
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    if command == 4:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    if command == 5:
        print(len(deq))
    if command == 6:
        if len(deq):
            print(0)
        else:
            print(1)
    if command == 7:
        if len(deq):
            print(deq[0])
        else:
            print(-1)
    if command == 8:
        if len(deq):
            print(deq[len(deq)-1])
        else:
            print(-1)

deq = deque()

n = int(input())

for _ in range(n):
    command_x_list = list(map(int, input().split()))
    command =0
    x= 0
    if command_x_list[0] == 1 or command_x_list[0] == 2:
        command = command_x_list[0]
        x = command_x_list[1]
        command_function(deq, command, x)
    else:
        command = command_x_list[0]
        command_function(deq, command)
    

