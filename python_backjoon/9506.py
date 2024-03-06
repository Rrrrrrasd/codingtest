def measure_list_make(n, check):
    measure_list = []
    while check < n:
        if n % check == 0:
            measure_list.append(check)
        
        check += 1

    return measure_list

n = 0
while True:
    n = int(input())
    if n == -1:
        break
    measure_list = measure_list_make(n, 1)

    if sum(measure_list) == n:
        s = str(n) + " = "
        for num in measure_list:
            s = s + str(num) + " + "
        print(s[:-3])
    else:
        print(n ,"is NOT perfect.")
            
















