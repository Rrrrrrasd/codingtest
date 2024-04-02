import sys
input = sys.stdin.readline

n = int(input())
result = list()

for _ in range(n):
    result.clear()
    world_list = list(map(list,(input().split())))
    for i in range(len(world_list)):
        world_list[i].reverse()
    
    for i in range(len(world_list)):
        result.append(''.join(world_list[i]))
    
    print(' '.join(result))