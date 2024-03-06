import math

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


n = int(input())
count = 0

num_list = list(map(int, input().split()))

for num in num_list:
    prime_check = is_prime_number(num)
    if prime_check:
        count += 1

print(count)

