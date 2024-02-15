import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*3 for _ in range(N)]

def dfs(n,prev):
    if n == N:
        return 0
    if dp[n][prev] != -1:
        return dp[n][prev]
    ans = 1e9
    for i in range(3):
        if i != prev:
            ans = min(dfs(n+1,i)+arr[n][i],ans)
    dp[n][prev] = ans
    return dp[n][prev]

dfs(0,-1)
print(max(dp[0]))