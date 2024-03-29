import sys
n = map(int, input().split())
a = set(map(int, sys.stdin.readline().strip().split()))
b = set(map(int, sys.stdin.readline().strip().split()))

a_b = a-b
b_a = b-a

print(len(a_b) + len(b_a))


