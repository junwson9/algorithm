from collections import deque
def bfs():
    while q:
        ci,cj = q.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni, nj = ci+di, cj+dj
            if (0<= ni < N and 0<= nj < M) and arr[ni][nj] == 0:
                if v[ni][nj] > v[ci][cj]+1:
                    v[ni][nj] = v[ci][cj]+1
                    q.append((ni,nj))



M,N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
inf = M*N
v = [[inf]*M for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            v[i][j] = 0
            q.append((i,j))

bfs()
ans = 0
for i in range(N):
    for j in range(M):
        if v[i][j] == inf and arr[i][j] != -1:
            ans = -1
            break
        if v[i][j] != inf and ans != -1:
            if v[i][j] > ans:
                ans = v[i][j]
print(ans)