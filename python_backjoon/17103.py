import sys
input = sys.stdin.readline

check = [0]*2 + [1]*999999
for i in range(2, 1000001):
    if check[i]:
        for j in range(i*2, 1000001, i):
            check[j] = 0


n = int(input())
for _ in range(n):
    count = 0
    num = int(input())
    for i in range(2, num//2+1):
        if check[i] and check[num-i]:
            count += 1
    print(count)

