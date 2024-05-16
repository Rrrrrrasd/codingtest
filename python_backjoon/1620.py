import sys

def dict_check(keyword, dict:dict):
    return dict[int(keyword)]

def dict2_check(keyword, dict:dict):
    return str(dict[keyword])
    


n, m = map(int, sys.stdin.readline().split())

poketmon_dict = dict()
poketmon_dict2 = dict()
result_list = list()

for i in range(n):
    poketmon = sys.stdin.readline().strip()
    poketmon_dict[i+1] = poketmon
    poketmon_dict2[poketmon] = i+1

for _ in range(m):
    keyword = sys.stdin.readline().strip()
    if keyword.isdigit():
        result_list.append(dict_check(keyword, poketmon_dict))
    else:
        result_list.append(dict2_check(keyword,poketmon_dict2))


for s in result_list:
    print(s)
