def bfs(s):
    q = [s]
    visited[s] = 1
    while q:
        t = q.pop(0)
        for i in adjL[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


N, M = map(int, input().split())
adjL = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 0
for i in range(M):
    s, e = map(int, input().split())
    adjL[s].append(e)
    adjL[e].append(s)
for i in range(1,N+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1
print(cnt)