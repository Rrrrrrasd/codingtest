import math

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


n = int(input())
m = int(input())


prime_list = []

for num in range(n, m+1):
    if is_prime_number(num):
        prime_list.append(num)

if not len(prime_list):
    print(-1)
else:
    print(sum(prime_list))
    print(prime_list[0])






