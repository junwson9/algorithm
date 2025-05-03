import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N = int(input())
u,v = map(int,input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*(N+1)
ans = []
def dfs(cur,cnt):
    visited[cur] = True
    if cur == v:
        return cnt

    for nxt in graph[cur]:
        if not visited[nxt]:
            rlt = dfs(nxt,cnt+1)
            if rlt != -1:
                return rlt
    return -1

print(dfs(u,0))
