from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M:
                if v[ni][nj] == 0 and arr[ni][nj] != 0:
                    v[ni][nj] = 1
                    q.append((ni,nj))
                elif arr[ni][nj] == 0:
                    sea[ci][cj] += 1
    return 1



N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
year = 0
while True:
    ans = 0
    v = [[0]*M for _ in range(N)]
    sea = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and v[i][j] == 0:
                ans += bfs(i,j)

    for i in range(N):
        for j in range(M):
            arr[i][j] -= sea[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0

    if ans == 0:
        break
    if ans >= 2:
        ans = year
        break
    year += 1
print(ans)
