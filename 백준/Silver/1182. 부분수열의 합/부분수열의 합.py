import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N,S = map(int,input().split())
lst = list(map(int,input().split()))
ans = 0


def dfs(n,sm):
    global ans
    if n == N:
        if sm == S:
            ans += 1
        return

    dfs(n+1,sm+lst[n])
    dfs(n+1,sm)

if S == 0:
    ans -= 1

dfs(0,0)
print(ans)