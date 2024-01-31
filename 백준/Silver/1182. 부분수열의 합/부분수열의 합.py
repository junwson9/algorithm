import sys
input = sys.stdin.readline
N,S = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
tmp = []
def dfs(n,sm,idx,cnt):
    global ans
    if n == cnt:
        if sm == S:
            ans += 1
        return

    for i in range(idx,N):
        dfs(n+1,sm+lst[i],i+1,cnt)


for i in range(1,N+1):
    dfs(0,0,0,i)
print(ans)