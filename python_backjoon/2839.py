n = int(input())

if n % 5 ==0 :
    print(n//5)
else:
    count = 0
    while n > 0:
        n-=3
        count += 1
        if n % 5 == 0:
            count += n//5
            print(count)
            break
        if n == 1 or n==2:
            print(-1)
        if n ==0:
            print(count)
