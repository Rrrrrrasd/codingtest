from collections import deque
import sys
n = int(sys.stdin.readline())
deque = deque([i+1 for i in range(n)])

while len(deque) > 1:
    deque.popleft()
    deque.append(deque.popleft())


print(deque[0])



