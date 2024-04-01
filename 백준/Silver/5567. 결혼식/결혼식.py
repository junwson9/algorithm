import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
v = [-1]*(n+1)
def bfs(cur):
    q = deque()
    q.append(cur)
    v[cur] = 0
    while q:
        prev = q.popleft()
        for nxt in graph[prev]:
            if v[nxt] == -1:
                v[nxt] = v[prev]+1
                q.append(nxt)

bfs(1)
ans = 0
for check in v:
    if check == 1 or check == 2:
       ans += 1
print(ans)


