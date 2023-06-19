def dfs(n,idx,tmp):
    prev = 0
    if n == M:
        ans.append(tmp)
        return

    for i in range(idx,N):
        if lst[i] != prev:
            prev = lst[i]
            dfs(n+1,i,tmp+[lst[i]])


N,M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
tmp = []
ans = []
v = [0]*N
dfs(0,0,tmp)
for a in ans:
    print(*a)