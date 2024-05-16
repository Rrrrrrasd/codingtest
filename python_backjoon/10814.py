import sys

n = int(sys.stdin.readline())

name_list = []
for _ in range(n):
    age, name = input().split()
    age = int(age)
    name_list.append([age, name])

name_list.sort(key=lambda x: x[0])


for age, name in name_list:
    print(age, name)