import sys
n = int(input())

num_list = list(map(int, sys.stdin.readline().rstrip().split()))
sorted_num_list = sorted(list(set(num_list)))

dic = {}

for i in range(len(sorted_num_list)):
    dic[sorted_num_list[i]] = i


for num in num_list:
    print(dic[num], end=" ")













