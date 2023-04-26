def dfs(n,tmp):
    if n == M:
        ans.append(tmp)
        return

    for i in range(len(lst)):
        dfs(n+1,tmp+[lst[i]])


N, M = map(int, input().split())
lst = [i for i in range(1,N+1)]
ans = []
tmp = []
dfs(0,tmp)
for rlt in ans:
    print(*rlt)