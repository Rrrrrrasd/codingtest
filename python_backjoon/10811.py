N, M = map(int, input().split())
basket = []
for i in range(1,N+1):
    basket.append(i)


for _ in range(M):
    i, j = map(int, input().split())
    temp = []
    for x in range(j-i+1):
        temp.append(basket[i+x-1])
    temp = temp[::-1]

    
    for x in range(j-i+1):
        basket[i+x-1] = temp[x]

    temp.clear()
    




for i in range(N):
    print(basket[i], end = ' ')
