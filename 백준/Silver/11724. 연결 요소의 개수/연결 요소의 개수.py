import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
v = [False]*(N+1)
def dfs(cur):
    v[cur] = True
    for nxt in graph[cur]:
        if not v[nxt]:
            dfs(nxt)

ans = 0
for i in range(1,N+1):
    if v[i]:
        continue
    dfs(i)
    ans += 1
print(ans)
