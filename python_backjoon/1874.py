from collections import deque
import sys

input = sys.stdin.readline
stack = deque()

n = int(input())
count = 1
result = list()
is_no = False

for _ in range(n):
    order_num = int(input())

    while count <= order_num:
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] == order_num:
        stack.pop()
        result.append('-')
    else:
        is_no = True
        break

if is_no:
    print('NO')
else:
    print('\n'.join(result))