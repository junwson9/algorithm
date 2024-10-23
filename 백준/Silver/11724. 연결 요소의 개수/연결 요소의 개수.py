import sys

input = sys.stdin.readline
N,M = map(int,input().split())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int, input().split())
    adjL[s].append(e)
    adjL[e].append(s)


ans = 0
visited = [0]*(N+1)
def dfs(n):
    visited[n] = 1
    for v in adjL[n]:
        if visited[v] == 0:
            dfs(v)

for i in range(1,N+1):
    if visited[i] == 1:
        continue
    dfs(i)
    ans += 1
print(ans)