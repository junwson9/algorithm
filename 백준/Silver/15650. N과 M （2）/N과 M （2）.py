def dfs(n,tmp,idx):
    if n == M:
        ans.append(tmp)
        return

    for i in range(idx,N):
        dfs(n+1,tmp+[lst[i]],i+1)


N, M = map(int, input().split())
lst = [i for i in range(1,N+1)]
ans = []
tmp = []
dfs(0,tmp,0)
for lst in ans:
    print(*lst)