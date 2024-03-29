import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
m = int(input())
parent = [0]*(n+1)
d = [1]*(n+1)
def dfs(cur,prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        parent[nxt] = cur
        d[nxt] = d[cur]+1
        dfs(nxt,cur)

dfs(1,0)
def lca(a,b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a

for _ in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))


