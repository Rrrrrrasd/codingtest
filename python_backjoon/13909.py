n = int(input())
count = 0
x = 1
while x*x <= n:
    x += 1
    count += 1
print(count)