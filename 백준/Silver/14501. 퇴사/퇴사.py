import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
def dfs(n,sm):
    global ans
    if n == N:
        if ans < sm:
            ans = sm
        return

    if n+arr[n][0] <= N:
        dfs(n+arr[n][0],sm+arr[n][1])
    dfs(n+1,sm)
dfs(0,0)
print(ans)