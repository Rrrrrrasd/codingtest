import sys
from collections import deque
input = sys.stdin.readline

is_open_tag = False
s = input()
result = ""
stack = deque()

for c in s:
    if not is_open_tag:
        if c == ' ' or c == '\n':
            while stack:
                result += stack.pop()
            result += ' '
            
        else:
            if c == '<':
                is_open_tag = True
                while stack:
                    result += stack.pop()

            stack.append(c)
    else:
        stack.appendleft(c)
        if c =='>':
            is_open_tag = False
            while stack:
                result += stack.pop()


print(result)


