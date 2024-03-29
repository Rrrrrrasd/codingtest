a1, a0 = map(int, input().split())

c = int(input())
n = int(input())

fn = a1*n + a0
gn = n*c

if fn <= gn and a1 <= c:
    print(1)
else:
    print(0)