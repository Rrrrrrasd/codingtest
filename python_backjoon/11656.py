import sys
input = sys.stdin.readline

s = input().strip()

s_list = list()

for i in range(len(s)):
    s_list.append(s[i:])

s_list.sort()

for word in s_list:
    print(word)