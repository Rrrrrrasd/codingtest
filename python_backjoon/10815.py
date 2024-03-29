import sys
n = int(sys.stdin.readline())

num_list = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())

check_list = map(int, sys.stdin.readline().split())
check_map = dict()

for check_num in check_list:
    check_map[check_num] = 0

for num in num_list:
    if num in check_map:
        check_map[num] += 1

result = []

for val in check_map.values():
    result.append(val)
print(" ".join(map(str,result)))