import sys

def gcd(a, b):
    while b >0:
        r = a%b
        a = b
        b = r
    return a

def lcm(a,b):
    temp = a*b
    result = temp //gcd(a,b)
    return result


n = int(sys.stdin.readline())
result_list = list()

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result_list.append(lcm(a,b))

for num in result_list:
    print(num)