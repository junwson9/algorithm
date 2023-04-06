def dfs(n,cnt):
    global ans

    if cnt == 4:
        ans = 1
        return

    for i in adjL[n]:
        if v[i] == 0:
            v[i] = 1
            dfs(i, cnt+1)
            v[i] = 0



N, M = map(int, input().split())
adjL = [[] for _ in range(N)]
v = [0]*N
ans = 0
for _ in range(M):
    s,e = map(int, input().split())
    adjL[s].append(e)
    adjL[e].append(s)

for i in range(N):
    v[i] = 1
    dfs(i,0)
    v[i] = 0
    if ans == 1:
        break

print(ans)