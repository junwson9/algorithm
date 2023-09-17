import sys
def dfs(n,i):
    global ans
    if n == M:
        rlt = 0
        for hi,hj in home:
            dist = 2*N+1
            for ci,cj in select:
                dist = min(dist,abs(ci-hi)+abs(cj-hj))
            rlt += dist
        if rlt < ans:
            ans = rlt
        return
    for idx in range(i,K):
        select.append(chicken[idx])
        dfs(n+1,idx+1)
        select.pop()


input = sys.stdin.readline
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append((i,j))
        if arr[i][j] == 2:
            chicken.append((i,j))
K = len(chicken)
ans = 2*N*len(home)+1
select = []
for t in range(K):
    dfs(0,t)
print(ans)