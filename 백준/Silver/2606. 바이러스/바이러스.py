import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int ,input().split())
    adjL[s].append(e)
    adjL[e].append(s)

visited = [0]*(N+1)
visited[1] = 1
cnt = 0
def dfs(n):
    global cnt
    for v in adjL[n]:
        if visited[v] == 0:
            visited[v] = 1
            dfs(v)
            cnt += 1


dfs(1)
print(cnt)