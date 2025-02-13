import sys
import math
input = sys.stdin.readline
N = int(input())
lmt = int(math.sqrt(N))

dp = [float('inf')] * (N+1)
dp[0]=0


for n in range(N+1):
    for i in range(1,lmt+1):
        if n+i**2 > N:
            break
        dp[n+i**2] = min(dp[n+i**2],dp[n]+1)

print(dp[N])

# dp = [-1]*100001
#
# def dfs(n):
#     if n > N:
#         return 12356123476
#
#     if n == N:
#         return 0
#
#     if dp[n] != -1:
#         return dp[n]
#
#     ans = 1e9
#
#     for i in range(1,lmt+1):
#         ans = min(dfs(n+i**2)+1,ans)
#     dp[n] = ans
#     return dp[n]
#
#
# dfs(0)
# print(dp[0])