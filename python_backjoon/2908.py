a,b  = input().split()
a_num = int(a[::-1])
b_num = int(b[::-1])
if a_num > b_num:
    print(a[::-1])
else:
    print(b[::-1])