# import sys
# s = sys.stdin.readline().strip()

# s_str_list = []
# s_len = 1
# count_check = 0
# while s_len <= len(s):
#     for i in range(len(s)-count_check):
#         s_str_list.append(s[i:i+s_len])
#     s_len += 1
#     count_check+=1

# print(len(set(s_str_list)))


import sys

word = sys.stdin.readline().strip()
S = list()

for i in range(0, len(word)):
    for j in range(i+1, len(word)+1):
        S.append(word[i:j])

S = set(S)
print(len(S))


