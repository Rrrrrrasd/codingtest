# from collections import deque
n, k = map(int, input().split())

# deq = deque()

# for i in range(n):
#     deq.append(i+1)


# result = list()

# while len(deq) != 0:
#     for _ in range(k-1):
#         deq.append(deq.popleft())
#     result.append(str(deq.popleft()))

# print('<' +', '.join(result) + '>')

idx = 0

queue = list()

for i in range(n):
    queue.append(i+1)
result = []

while queue:
    idx += k-1
    if idx >= len(queue):
        idx %= len(queue)
    result.append(str(queue.pop(idx)))

print('<' +', '.join(result) + '>')

