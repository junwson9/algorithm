def dfs(n,tmp):
    prev = 0
    if n == M:
        ans.append(tmp)
        return

    for i in range(N):
        if v[i] == 0 and prev != lst[i]:
            v[i] = 1
            prev = lst[i]
            dfs(n+1,tmp+[lst[i]])
            v[i] = 0


N,M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
tmp = []
ans = []
v = [0]*N
dfs(0,tmp)
for a in ans:
    print(*a)