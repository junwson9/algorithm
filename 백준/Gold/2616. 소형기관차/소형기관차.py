import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N = int(input())
lst = list(map(int,input().split()))
M = int(input())

dp = [[-1]*4 for _ in range(N+1)]

prefix = [0]*(N+1)
for i in range(N):
    prefix[i+1] = prefix[i]+lst[i]

def dfs(n,idx):
    if n == 3 or idx >= N:
        return 0

    if dp[idx][n] != -1:
        return dp[idx][n]


    if idx+M <= N:
        dp[idx][n] = max(dfs(n,idx+1),dfs(n+1,idx+M)+(prefix[idx+M]-prefix[idx]))
    else:
        dp[idx][n] = dfs(n,idx+1)

    return dp[idx][n]

print(dfs(0,0))




