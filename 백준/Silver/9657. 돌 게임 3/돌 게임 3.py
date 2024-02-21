import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N = int(input())
dp = [-1]*(N+1)
stone = [1,3,4]
def dfs(n):
    if n == 0:
        return False
    if n < 0:
        return True

    if dp[n] != -1:
        return dp[n]
    cnt = 0
    for i in stone:
        if not dfs(n-i):
           cnt += 1
    if cnt > 0:
        dp[n] = True
    else:
        dp[n] = False
    return dp[n]

dfs(N)
if dp[N] == True:
    print('SK')
else:
    print('CY')


