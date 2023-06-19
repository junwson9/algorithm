def dfs(n,tmp):
    if n == M:
        ans.append(tmp)
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1,tmp+[lst[i]])
            v[i] = 0


N,M = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
tmp = []
v = [0]*N
dfs(0,tmp)
ans.sort()
for a in ans:
    print(*a)
