from collections import deque
import sys
input = sys.stdin.readline

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


def stack_order(stack:deque, order_list:list):
    order = order_list[0]
    if order == 'push':
        x = int(order_list[1])
        stack.append(x)
    
    if order == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    if order == 'size':
        print(len(stack))
    
    if order =='empty':
        if stack:
            print(0)
        else:
            print(1)

    if order == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)





n = int(input())
stack = deque()

for _ in range(n):
    order_list = list(map(str, input().split()))
    stack_order(stack, order_list)
    