from collections import deque
import sys
input = sys.stdin.readline

stack_queue_n = int(input())

stack_queue_check = list(map(int, input().strip().split()))
stack_queue_value = list(map(int, input().strip().split()))

stack_queue_deq = deque()

value_n = int(input())
input_values = list(map(int, input().strip().split()))

for i in range(stack_queue_n):
    if stack_queue_check[i] ==0:
        stack_queue_deq.appendleft(stack_queue_value[i])


for i in range(value_n):
    stack_queue_deq.append(input_values[i])
    print(stack_queue_deq.popleft(), end=' ')






