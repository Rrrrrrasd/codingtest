p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))
p4 = []

if p1[0] == p2[0]:
    p4.append(p3[0])
else:
    if p2[0] == p3[0]:
        p4.append(p1[0])
    else:
        p4.append(p2[0])

if p1[1] == p2[1]:
    p4.append(p3[1])
else:
    if p2[1] == p3[1]:
        p4.append(p1[1])
    else:
        p4.append(p2[1])

print(p4[0], p4[1])