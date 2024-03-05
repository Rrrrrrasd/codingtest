n =  int(input())
draw = [[0 for col in range(100)] for row in range(100)]
result = 0

for _ in range(n):
    w, h = map(int, input().split())
    for i in range(w, w+10):
        for j in range(h, h+10):
            draw[i][j] = 1


for i in range(100):
    for j in range(100):
        if draw[i][j] == 1:
            result += 1

print(result)

