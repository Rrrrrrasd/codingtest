s = input()
s = s.upper()

countList = {}
maxnum = 0
result = ""

for char in s:
    if char in countList:
        countList[char] += 1
    else:
        countList[char] = 1


for val in countList.values():
    if val > maxnum:
        maxnum = val

for key, val in countList.items():
    if val == maxnum:
        if result:
            result = "?"
            break
        else:
            result = key
    
    
    

print(result)

