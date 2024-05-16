import sys
input = sys.stdin.readline


a,b,c,d, = input().strip().split()

num1 = str(a)+str(b)
num2 = str(c)+str(d)

print(int(num1)+ int(num2))
