import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
v = [False]*(n+1)

def dfs(cur):
    v[cur] = True
    for nxt in graph[cur]:
        if not v[nxt]:
            dfs(nxt)


dfs(1)
ans = 0
for i in range(2,n+1):
    if v[i]:
        ans += 1
print(ans)



