num = int(input())
money_list = [25, 10, 5, 1]

for _ in range(num):
    money = int(input())
    for i in money_list:
        print(money//i, end=' ')
        money = money%i
    print()
