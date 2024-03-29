def check_num_list(num_list):
    if num_list[0]+num_list[1] <= num_list[2]:
        print("Invalid")
    else:
        if num_list[0] == num_list[1] == num_list[2]:
            print("Equilateral")
        elif num_list[0] == num_list[1] or num_list[1] == num_list[2] or num_list[2] == num_list[0]:
            print("Isosceles")
        else:
            print("Scalene")


while True:
    num_list = list(map(int,input().split()))

    if not sum(num_list):
        break
    num_list.sort()

    check_num_list(num_list)


