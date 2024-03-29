import sys

n, m = map(int, sys.stdin.readline().split())
s_map = dict()
count = 0

for _ in range(n):
    s = sys.stdin.readline().strip()
    s_map[s] = 0

for _ in range(m):
    s = sys.stdin.readline().strip()
    if s in s_map:
        s_map[s] += 1

for val in s_map.values():
    count += val




print(count)





