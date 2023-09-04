from collections import deque

def bfs(i,j,size):
    v = [[-1]*N for _ in range(N)]
    temp = []
    q = deque()
    q.append((i,j))
    v[i][j] = 0
    while q:
        t = q.popleft()
        for di,dj in ((-1,0),(0,-1),(1,0),(0,1)):
            ni,nj = t[0]+di,t[1]+dj
            if 0<= ni< N and 0<= nj < N and v[ni][nj] == -1:
                if arr[ni][nj] <= size:
                    q.append((ni,nj))
                    v[ni][nj] = v[t[0]][t[1]]+1
                    if arr[ni][nj] < size and arr[ni][nj] != 0:
                        temp.append((ni,nj,v[ni][nj]))
        temp.sort(key=lambda x:(-x[2],-x[0],-x[1]))
    return temp


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
si = sj = 0
ans = 0
cnt = 0
size = 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si,sj = i,j
while True:
    shark = bfs(si,sj,size)
    if len(shark) == 0:
        break
    nx, ny, dis = shark.pop()
    ans += dis
    arr[si][sj],arr[nx][ny] = 0,0
    si,sj = nx,ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(ans)


