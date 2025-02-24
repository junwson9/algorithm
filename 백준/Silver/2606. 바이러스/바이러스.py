import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
adjL = [[] for _ in range(N+1)]

for _ in range(M):
    s,e = map(int,input().split())
    adjL[s].append(e)
    adjL[e].append(s)

visited = [0]*(N+1)

def dfs(n):

    for v in adjL[n]:
        if not visited[v]:
            visited[v] = 1
            dfs(v)
dfs(1)
cnt = 0
for i in range(2,N+1):
    if visited[i]:
        cnt += 1


print(cnt)