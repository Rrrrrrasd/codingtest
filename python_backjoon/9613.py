import sys
input = sys.stdin.readline

def gcd(a, b):
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


n = int(input())

for _ in range(n):
    num_list = list(map(int, input().split()))
    num_list = num_list[1:]
    num_list = sorted(list(num_list))
    gcd_sum = 0
    idx1 = 0
    idx2 = 1

    while idx1 < len(num_list)-1:
        gcd_sum += (gcd(num_list[idx1], num_list[idx2]))
        
        idx2 += 1
        if idx2 >= len(num_list):
            idx1 += 1
            idx2 = idx1 + 1

    print(gcd_sum)





