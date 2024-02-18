import sys
input = sys.stdin.readline
N = int(input())
ans = 0
dp = [-1]*1001
def dfs(n):
    global ans
    if n > N:
        return 0

    if n == N:
        return 1

    if dp[n] != -1:
        return dp[n]
    ans = (dfs(n+1)+dfs(n+2)) % 10007
    dp[n] = ans
    return dp[n]
dfs(0)
print(dp[0])