n = int(input())


for i in range(1, n+1):
    temp = sum(map(int, str(i)))
    temp += i

    if temp == n:
        print(i)
        break

    if i == n:
        print(0)



