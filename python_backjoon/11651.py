n = int(input())

coordinate_list = []

# for _ in range(n):
#     coordinate = list(map(int, input().split()))
    
#     coordinate_list.append(coordinate)


# coordinate_list = sorted(coordinate_list, key=lambda x : (x[1], x[0]))


# for nums in coordinate_list:
#     temp = ' '.join(str(num) for num in nums)
#     print(temp)



for _ in range(n):
    x, y = map(int, input().split())
    coordinate_list.append([y,x])

coordinate_list = sorted(coordinate_list)

for y,x in coordinate_list:
    print(x, y)