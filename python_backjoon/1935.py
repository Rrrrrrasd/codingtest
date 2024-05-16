from collections import deque

import sys
input = sys.stdin.readline


n = int(input())
e_list = input().strip()
stack = deque()
e_dict = dict()

for i in range(n):
    e_dict[chr(ord('A')+i)] = int(input())


for e in e_list:
    if e in ['+','-','/','*']:
        b = stack.pop()
        a = stack.pop()
        if e == '+':
            a += b
        if e =='-':
            a-= b
        if e =='*':
            a *= b
        if e == '/':
            a/=b
        stack.append(a)
    else:
        stack.append(e_dict[e])

result = float(stack.pop())
print(f'{result:.2f}')

