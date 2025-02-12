import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

dp = [-99999]*(N+100)

dp[N] = 0

for i in range(N-1,-1,-1):
    dp[i] = max(dp[i+1],dp[i+arr[i][0]]+arr[i][1])

print(dp[0])


# def dfs(n):
#     if n > N:
#         return -12375891236754367
#
#     if n == N:
#         return 0
#
#     if dp[n] != -1:
#         return dp[n]
#
#     dp[n] = max(dfs(n+1),dfs(n+arr[n][0])+arr[n][1])
#     return dp[n]
#
# dfs(0)
