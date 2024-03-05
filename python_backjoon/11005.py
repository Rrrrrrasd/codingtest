n, b = map(int, input().split())

num = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

result_list =[]

while n >= b:
    temp = n % b
    result_list.append(num[temp])
    n = n // b

result = "".join(reversed(result_list))
result = num[n] + result
print(result)



