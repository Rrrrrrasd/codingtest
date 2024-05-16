import sys
input = sys.stdin.readline


n = int(input())
if n == 0:
    print(n)
else:
    res =''
    while n:
        if n%(-2):
            res = '1' + res
            n = n//-2 + 1
            print(n)
        else:
            res = '0' + res
            n //= -2
            print(n)
    print(res)

    print(1/-2)


