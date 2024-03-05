n = 5

world_procession = [["*" for _ in range(15)] for _ in range(5)]
result = ""

for i in range(n):
    world = input()
    for j in range(len(world)):
        world_procession[i][j] = world[j]


for j in range(15):
    for i in range(n):
        if world_procession[i][j] != "*":
            result += world_procession[i][j]
        

print(result)






