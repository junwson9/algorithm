import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
lst = list(map(int,input().split()))
dp = [[-1]*501 for _ in range(501)]
def dfs(n1,n2):
    if n1 < 0 or n2 < 0:
        return 0
    if dp[n1][n2] != -1:
        return dp[n1][n2]
    for i in lst:
        if not dfs(n1-i,n2) and n1-i >= 0:
            dp[n1][n2] = 1
            return dp[n1][n2]
    for j in lst:
        if not dfs(n1,n2-j) and n2-j >= 0:
            dp[n1][n2] = 1
            return dp[n1][n2]
    dp[n1][n2] = 0
    return dp[n1][n2]

for _ in range(5):
    x,y = map(int,input().split())
    dfs(x,y)
    if dp[x][y]:
        print('A')
    else:
        print('B')




