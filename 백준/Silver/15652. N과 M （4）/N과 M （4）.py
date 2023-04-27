def dfs(n,tmp,idx):
    if n == M:
        rlt.append(tmp)
        return

    for i in range(idx, N):
        dfs(n+1,tmp+[lst[i]],i)

N, M = map(int, input().split())
lst = [i for i in range(1,N+1)]
rlt = []
tmp = []
dfs(0,tmp,0)
for ans in rlt:
    print(*ans)