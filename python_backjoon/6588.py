import sys
import math
input = sys.stdin.readline


def goldbahu_find(n, erasto):
    prime_list = list()
    for i in range(n-3, 2, -2):
        if erasto[i] and erasto[n-i]:
            print(f"{n} = {n-i} + {i}")
            return True

    return False


#에라스토테네스 체 전처리
erstotenesu = [1]*1000000

for i in range(2, int(math.sqrt(1000000))+1):
    if erstotenesu[i] == 1:
        for j in range(i+i, 1000000, i):
            erstotenesu[j] = 0


while True:
    n = int(input().strip())
    if n == 0:
        break

    if not goldbahu_find(n, erstotenesu):
        print("Goldbach's conjecture is wrong.")
    