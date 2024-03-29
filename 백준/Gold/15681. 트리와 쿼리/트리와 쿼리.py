import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N,R,Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
sz = [1]*(N+1)
def dfs(cur, prev):
    for nxt in tree[cur]:
        if nxt == prev:
            continue
        dfs(nxt,cur)
        sz[cur] += sz[nxt]
dfs(R,0)
for _ in range(Q):
    u = int(input())
    print(sz[u])

