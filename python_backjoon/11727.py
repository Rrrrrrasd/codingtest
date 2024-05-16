import sys
input = sys.stdin.readline

n = int(input())

#bottom-up
dp = [0] * 1001
dp[1] = 1 # n = 1일떄 타일을 채우는 경우
dp[2] = 3 # n = 2일때 타일을 채우는 경우

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 10007 

print(dp[n])