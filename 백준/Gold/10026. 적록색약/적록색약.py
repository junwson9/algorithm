from collections import deque
def bfs(i,j):
    global R_cnt,G_cnt,B_cnt
    q = deque()
    q.append((i,j))
    v[i][j] = 1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = di+ci,dj+cj
            if 0<= ni < N and 0<= nj < N:
                if arr[ni][nj] == arr[ci][cj] and v[ni][nj] == 0:
                    v[ni][nj] = 1
                    q.append((ni,nj))
    if arr[i][j] == 'R':
        R_cnt += 1
    if arr[i][j] == 'G':
        G_cnt += 1
    if arr[i][j] == 'B':
        B_cnt += 1


def bfs2(i,j):
    global cnt
    q = deque()
    q.append((i,j))
    v2[i][j] = 1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = di+ci,dj+cj
            if 0<= ni < N and 0<= nj < N:
                if arr[ni][nj] == arr[ci][cj] and v2[ni][nj] == 0:
                    v2[ni][nj] = 1
                    q.append((ni,nj))
    cnt += 1


N = int(input())
arr = [list(input()) for _ in range(N)]
v = [[0]*N for _ in range(N)]
v2 = [[0]*N for _ in range(N)]
R_cnt = G_cnt = B_cnt = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if v[i][j] == 0:
            bfs(i,j)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if v2[i][j] == 0:
            bfs2(i,j)
print(R_cnt+G_cnt+B_cnt,cnt)
