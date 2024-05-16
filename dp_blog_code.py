#Top-Down
# dp = [-1] * 100

# def fib(n:int):
#     if n == 0: return 0
#     if n == 1: return 1
#     if n == 2: return 1

#     if dp[n] != -1: return dp[n]

#     dp[n] = fib(n-1) + fib(n-2)
#     return dp[n]

# print(fib(50))

#Bottom-Up
dp = [-1] * 100
dp[1] = 1
dp[2] = 1
n = 50

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])