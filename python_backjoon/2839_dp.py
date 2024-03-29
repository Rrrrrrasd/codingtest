dp = [0 for i in range(5001)]

n = int(input())

dp[3] = 1
dp[5] = 1

for i in range(6, n+1):
    if dp[i - 3]:
        dp[i] = dp[i-3]+1
    if dp[i-5]:
        if dp[i]:
            dp[i] = min(dp[i], dp[i-5]+1)
        else:
            dp[i] =dp[i-5] + 1

if dp[n] != 0:
    print(dp[n])
else:
    print(-1)