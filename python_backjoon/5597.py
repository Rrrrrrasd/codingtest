students = []

for i in range(30):
    students.append(i+1)

for _ in range(28):
    i = int(input())
    students.remove(i)


for num in students:
    print(num, end=' ')



