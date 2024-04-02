import sys
from collections import deque
input = sys.stdin.readline

primary = input().strip()
stack = deque()
result = ''
priority_dict= {'*':2, '+':1, '-':1, '/':2, '(':0}

for s in primary:
    
    if s >= 'A' and  s<='Z':
        result += s
        continue

    if len(stack) == 0 or s =='(':
        stack.append(s)
        continue

    if s ==')':
        while stack[-1] != '(':
            result += stack.pop()
        stack.pop()
        continue

    if s in priority_dict and stack[-1] in priority_dict:
        if priority_dict[stack[-1]] < priority_dict[s]:
            stack.append(s)
        else:
            while not len(stack)==0 and priority_dict[stack[-1]] >= priority_dict[s]:
                result += stack.pop()
            stack.append(s)

while not len(stack) ==0 :
    result += stack.pop()
        

    
print(result) 