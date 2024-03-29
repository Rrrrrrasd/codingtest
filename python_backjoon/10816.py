import sys
n = int(sys.stdin.readline().strip())
have_card = list(sys.stdin.readline().split())

n = int(sys.stdin.readline().strip())
check_card = list(sys.stdin.readline().split())

check_card_map = dict()
result = list()

for num in check_card:
    check_card_map[num] = 0

for num in have_card:
    if num in check_card_map:
        check_card_map[num] += 1


# for check in check_card:
#     if check in check_card_map:
#         print(check_card_map[check], end=' ')
#     else:
#         print(0, end=' ')

for check in check_card:
    print(check_card_map[check], end=' ')










