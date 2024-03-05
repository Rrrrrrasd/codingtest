n, m = map(int, input().split())

procession_1 = []
procession_2 = []
result = []

for _ in range(n):
    temp  = list(map(int, input().split()))
    procession_1.append(temp)

for _ in range(n):
    temp  = list(map(int, input().split()))
    procession_2.append(temp)

for i in range(n):
    temp = []
    for j in range(m):
        temp.append(procession_1[i][j] + procession_2[i][j])
    result.append(temp)

for i in range(n):
    for j in range(m):
        print(result[i][j], end=" ")
    print()
    