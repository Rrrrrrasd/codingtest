import sys
from collections import deque
input = sys.stdin.readline
stack= deque()
word = ''
while True:
    
    word = input().rstrip()

    if word == '.':
        break
    
    for s in word:
        if s == '[':
            stack.append(s)
            
        if s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
                
            else:
                print('no')
                break
        
        if s== '(':
            stack.append(s)
            
        if s==')':
            if stack and stack[-1] == '(':
                stack.pop()
                
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')

    stack.clear()

    


