import sys
input = sys.stdin.readline


while True:
    line = input().rstrip('\n')

    if not line:
        break

    l, u, d, sp = 0, 0, 0, 0

    for s in line:
        if s.islower():
            l += 1
        if s.isupper():
            u += 1
        if s.isdigit():
            d += 1
        if s.isspace():
            sp += 1

    print(l,u,d,sp)


