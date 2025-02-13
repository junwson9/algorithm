import sys
sys.setrecursionlimit(10**3)
input = sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))

dp = [[0]*5001 for _ in range(5001)]


for length in range(2,N+1):
    for l in range(N-length+1):
        r = l+length-1
        if lst[l] == lst[r]:
            dp[l][r] = dp[l+1][r-1]
        else:
            dp[l][r] = min(dp[l+1][r],dp[l][r-1])+1

print(dp[0][N-1])


# def dfs(l,r):
#     if l >= r:
#         return 0
#
#     if dp[l][r] != -1:
#         return dp[l][r]
#
#
#     if lst[l] == lst[r]:
#         dp[l][r] = dfs(l+1,r-1)
#
#     else:
#         dp[l][r] = min(dfs(l+1,r),dfs(l,r-1))+1
#     return dp[l][r]
#
# print(dfs(0,N-1))