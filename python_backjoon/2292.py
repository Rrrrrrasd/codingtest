n = int(input())

comb_count = 1
count = 1

while n > comb_count:
    comb_count += 6 * count
    count += 1

print(count)