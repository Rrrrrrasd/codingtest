from collections import deque
import sys
input = sys.stdin.readline


n, k = map(int, input().strip().split())

deq = deque(i+1 for i in range(n))
result = list()
k_count = 1

while deq:
    for _ in range(k-1):
        deq.append(deq.popleft())
    result.append(deq.popleft())


print('<' + ', '.join(map(str,result))+'>')
    
