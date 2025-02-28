import sys
input = sys.stdin.readline
n,k = map(int,input().split())
lst = list(int(input().rstrip()) for _ in range(n))
dp = [[-1] * (k + 1) for _ in range(n)]

def dfs(i, sm):
    if sm == 0:
        return 1
    if sm < 0 or i >= n:
        return 0
    if dp[i][sm] != -1:
        return dp[i][sm]

    dp[i][sm] = dfs(i+1, sm) + dfs(i, sm - lst[i])
    return dp[i][sm]


print(dfs(0, k))
