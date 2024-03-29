a, b, c, d, e, f = map(int, input().split())

# 연립 방정식 풀이
# x = (c*e-b*f)/(a*e-b*d)
# y = (c*d-a*f)/(b*d-a*e)

# print(int(x), int(y))


for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y ==f:
            print(x, y)
            break
        
