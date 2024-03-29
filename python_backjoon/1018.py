n, m = map(int, input().split())

chess = [input() for _ in range(n)]

str1 = 'WBWBWBWB'
str2 = 'BWBWBWBW'
w_board = [str1,str2,str1,str2,str1,str2,str1,str2]
b_board = [str2,str1,str2,str1,str2,str1,str2,str1]


def check(i, j):
    result_w = 0
    result_b = 0

    for di in range(8):
        for dj in range(8):
            ni, nj = i+di, j+dj
            if chess[ni][nj] != w_board[di][dj]:
                result_w += 1
            if chess[ni][nj] != b_board[di][dj]:
                result_b += 1

    return min(result_w, result_b)

result =  1000000

for i in range(n-7):
    for j in range(m-7):
        result = min(result, check(i, j))

print(result)


    