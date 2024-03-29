import math
import sys
input = sys.stdin.readline

n = int(input())
a = int(input())
arr = list()

for _ in range(n-1):
    num = int(input())
    arr.append(num-a)
    a = num

g = arr[0]
for j in range(1, len(arr)):
    g = math.gcd(g, arr[j])

result = 0
for num in arr:
    result += (num//g)-1

print(result)
