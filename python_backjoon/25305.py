n, k = map(int, input().split())


member = list(map(int, input().split()))

temp = sorted(member, reverse=True)

print(temp[k-1])