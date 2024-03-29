n, m = map(int, input().split())

card_list = list(map(int, input().split()))

max_card_list_sum = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            temp = card_list[i] + card_list[j] + card_list[k]
            if temp <= m and temp > max_card_list_sum:
                max_card_list_sum = temp


print(max_card_list_sum)

