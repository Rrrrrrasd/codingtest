import sys

input = sys.stdin.readline

n = int(input())
dp = {1:1, 2:1}

def topDown(n:int):
    if n in dp:
        return dp[n]
    
    result = (topDown(n-2) + topDown(n-1))
    dp[n] = result
    return result

print(topDown(n))


