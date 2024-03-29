import sys
n=int(sys.stdin.readline())

point = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


point.sort()

for x in point:
    print(' '.join(map(str, x)))

 
