num = int(input())
result = 0
str_list = []
check_list = []
break_check = False


for _ in range(num):
    s = input()
    str_list.append(s)
        


for str in str_list:
    check_list.clear()
    break_check = False
    p1 = 0
    p2 = 1
    list_str = list(str)
    while p2 < len(list_str):
        if list_str[p2] in check_list:
            break_check = True
            break
        else:
            if list_str[p1] != list_str[p2]:
                check_list.append(list_str[p1])
        p1 += 1
        p2 += 1

        
    if not break_check:
        result += 1

print(result)


            
        
        
        
