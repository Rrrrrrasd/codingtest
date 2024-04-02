import sys
input = sys.stdin.readline
alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s = input().strip()
count_list = [0]*26

for alhp in s:
    if alhp in alpha_list:
        count_list[alpha_list.index(alhp)] += 1
        

print(*count_list)
