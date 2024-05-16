import sys
input = sys.stdin.readline

n = int(input())

#bottom-up
dp = [0] * 1001
dp[1] = 1 # n = 1일떄 타일을 채우는 경우
dp[2] = 2 # n = 2일때 타일을 채우는 경우


for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007 

print(dp[n])


#top-down
import sys
sys.setrecursionlimit(10**7)#재귀를 여러번 할 수 있게 해줌
input = sys.stdin.readline

n = int(input())

dp = {}

def topDown(n: int):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    
    if n in dp:
        return dp[n]
    
    result = (topDown(n-1) + topDown(n-2)) % 10007
    dp[n] = result
    return result


print(topDown(n))
#https://www.youtube.com/watch?v=HmvD3X5pme8
#https://www.youtube.com/watch?v=6C2KwWlpMh4