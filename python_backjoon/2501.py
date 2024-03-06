num, n = map(int, input().split())

check = 1
measure_list = []

while num >= check:
    if num % check == 0 :
        measure_list.append(check)
    check += 1

if len(measure_list) < n:
    print(0)
else:
    print(measure_list[n-1])
