
def gcd(a,b):
    while b > 0:
        r = a%b
        a = b
        b = r
    return a


def lcm(a,b):
    temp = a*b
    result = temp//gcd(a,b)
    return result


a, b = map(int,input().split())
print(lcm(a,b))