import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [-9999]*(N+53)
dp[N] = 0
for i in range(N-1,-1,-1):
    dp[i] = max(dp[i+1],dp[i+arr[i][0]]+arr[i][1])
print(dp[0])