import sys

def sum_fraction(a1, b1, a2, b2):
    a = 0
    b = 0
    if b1 == b2:
        a = a1+a2
        b = b1
        return a, b
    else:
        a = (a1*b2)+(a2*b1)
        b = b1*b2
        return a, b
    
def gcd(a, b):
    while b >0:
        r = a%b
        a = b
        b = r
    return a

def make_irreducible_fraction(a,b):
    g = gcd(a,b)
    a= a//g
    b= b//g
    return a,b


input = sys.stdin.readline
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

a, b= map(int, sum_fraction(a1,b1,a2,b2))
a, b = map(int, make_irreducible_fraction(a,b))

print(a,b)



