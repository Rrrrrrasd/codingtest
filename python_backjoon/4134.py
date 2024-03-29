import math
import sys
def search_prime(x):
    if x ==0:
        return False
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0: 
            return False
    return True


n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())-1
    is_search_prime = False
    while not is_search_prime:
        num += 1
        is_search_prime = search_prime(num)
        
    print(num)