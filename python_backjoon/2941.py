check_croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]
s = list(input())
check_str = ""
result = []
idx_0 = 0
idx_1 = 1
idx_2 = 2

while(idx_1 < len(s)):
    check_str = s[idx_0] + s[idx_1]
    if check_str in check_croatia:
        result.append(check_str)
        idx_0 += 2
        idx_1 += 2
        idx_2 += 2
    else:
        if idx_2 < len(s):
            check_str += s[idx_2]
            if check_str in check_croatia:
                result.append(check_str)
                idx_0 += 3
                idx_1 += 3
                idx_2 += 3
            else:
                result.append(s[idx_0])
                idx_0 += 1
                idx_1 += 1
                idx_2 += 1
        else:
            result.append(s[idx_0])
            idx_0 += 1
            idx_1 += 1
            idx_2 += 1

if idx_0 == len(s)-1:
        result.append(s[idx_0])

check_str = ""
    
print(len(result))

    
    



    

