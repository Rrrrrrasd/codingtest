def gcd(a, b):
    r = 0
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a
def lcm(a,b):
    return(a*b)/gcd(a,b)

a, b = map(int,input().split())

if a < b:
    temp = b
    b = a
    a = temp

print(gcd(a,b))
print(int(lcm(a,b)))

