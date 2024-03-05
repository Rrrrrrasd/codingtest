a, b, v = map(int, input().split())

q = (v-a)//(a-b)
r = (v-a)%(a-b)

if r == 0:
    print(q+1)
else:
    print(q+2)