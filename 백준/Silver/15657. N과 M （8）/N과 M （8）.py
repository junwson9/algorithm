def dfs(n,idx,tmp):
    if n == M:
        ans.append(tmp)
        return
    for i in range(idx,N):
        dfs(n+1,i,tmp+[lst[i]])


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
tmp = []
ans = []
dfs(0,0,tmp)
for a in ans:
    print(*a)