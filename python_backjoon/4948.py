import sys
import math
input = sys.stdin.readline

check = [0]*2+[1]*246912
for i in range(2, 246913):
    if check[i]:
        for j in range(i*2, 246913, i):
            check[j] = 0


while True:
    x = int(input())
    if x==0:
        break
    print(sum(check[x+1:x*2+1]))














# finished_prime_search = {1:False}

# def prime_search(x):
#     if x in finished_prime_search:
#         return finished_prime_search[x]
    
#     for i in range(2, int(math.sqrt(x))+1):
#         if x % i ==0 :
#             finished_prime_search[x] = False
#             return False
#     finished_prime_search[x] = True
#     return True
    
# while True:
#     n = int(input())
#     count = 0
#     if n == 0:
#         break

#     for num in range(n+1, (2*n)+1):
#         if prime_search(num):
#             count += 1
#     print(count)



    

