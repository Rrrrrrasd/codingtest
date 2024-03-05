n, b = input().split()

n = "".join(reversed(n))
b = int(b)

sum = 0

num = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


for i in range(len(n)):
    temp = num.index(n[i]) * (b ** i)
    sum += temp

print(sum)





