import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N,a,b = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v,cost = map(int,input().split())
    graph[u].append([v,cost])
    graph[v].append([u,cost])

v = [False]*(N+1)

def dfs(cur,tmp,mx):
    v[cur] = True
    if cur == b:
        print(tmp-mx)
    for nxt,cost in graph[cur]:
        if not v[nxt]:
            dfs(nxt,tmp+cost,max(cost,mx))

if a == b:
    print(0)
else:
    dfs(a,0,0)