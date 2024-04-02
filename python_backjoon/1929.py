import sys
import math

def prime_number_search(x):
    if x == 1:
        return False
    
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


input = sys.stdin.readline
m, n = map(int, input().split())

for num in range(m, n+1):
    if prime_number_search(num):
        print(num)


