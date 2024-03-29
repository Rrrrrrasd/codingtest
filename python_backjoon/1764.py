import sys

n, m = map(int, sys.stdin.readline().split())

no_listen_human_set = set()
no_look_human_set = set()
for _ in range(n):
    name = sys.stdin.readline().strip()
    no_listen_human_set.add(name)

for _ in range(m):
    name = sys.stdin.readline().strip()
    no_look_human_set.add(name)

no_look_no_listen_human_list = list(no_listen_human_set & no_look_human_set)
no_look_no_listen_human_list.sort()

print(len(no_look_no_listen_human_list))
for name in no_look_no_listen_human_list:
    print(name)

 