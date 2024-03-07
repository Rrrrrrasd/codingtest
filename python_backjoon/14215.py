side_list = list(map(int, input().split()))

side_list.sort()


if side_list[0]+side_list[1] > side_list[2]:
    print(sum(side_list))
else:
    side_list[2] = side_list[0]+side_list[1]-1
    print(sum(side_list))


