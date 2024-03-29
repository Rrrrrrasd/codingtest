from collections import deque
import sys
input = sys.stdin.readline

def command_function(deq:deque ,command, x=0):
    if command == 1:
        deq.append(x)
    
    if command == 2:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    
    if command ==3:
        print(len(deq))

    if command ==4:
        if deq:
            print(0)
        else:
            print(1)
    
    if command ==5:
        if deq:
            print(deq[len(deq)-1])
        else:
            print(-1)


n = int(input())
stack = deque()

for _ in range(n):
    command_list = list(map(int, input().split()))
    command = 0
    x = 0
    if command_list[0] == 1:
        command = command_list[0]
        x = command_list[1]
        command_function(stack, command, x)
    else:
        command = command_list[0]
        command_function(stack, command)


    
    
