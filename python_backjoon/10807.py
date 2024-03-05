N = int(input())
nums = list(map(int, input().split()))
V = int(input())
counter = 0

for num in nums:
    if num == V:
        counter += 1

print(counter)
