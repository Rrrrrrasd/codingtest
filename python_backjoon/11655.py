import sys

input = sys.stdin.readline
code = input().rstrip('\n')
answer= ''

for i in range(len(code)):
    if code[i].isupper():
        temp = ord(code[i]) + 13
        if temp < ord('A') or temp > ord('Z'):
            temp -= 26
        answer += chr(temp)
        continue

    if code[i].islower():
        temp = ord(code[i]) + 13
        if temp < ord('a') or temp > ord('z'):
            temp -= 26
        answer += chr(temp)
        continue
    answer += code[i]


print(answer)
        


        
                


