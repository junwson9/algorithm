import sys

input = sys.stdin.readline

N,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
v = [0]*N
ans = -1e9

def dfs(n,tmp,idx):
    global ans
    if n == K:
        rlt = 0
        for n in tmp:
            for m in tmp:
                rlt += arr[n][m]

        ans = max(rlt,ans)
        return

    for i in range(idx,N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1,tmp+[i],i)
            v[i] = 0


dfs(0,[],0)

print(ans//2)