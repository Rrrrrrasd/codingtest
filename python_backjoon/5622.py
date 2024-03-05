d_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
s = list(input())

result = 0

for char in s:
    for d in d_list:
        if char in d:
            result += d_list.index(d) + 3

print(result)