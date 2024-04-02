import math
num_list = []
for _ in range(5):
    temp = int(input())
    num_list.append(temp)

num_list.sort()
print(int(sum(num_list)/len(num_list)))
idx = math.floor(len(num_list)//2) 
print(num_list[idx])