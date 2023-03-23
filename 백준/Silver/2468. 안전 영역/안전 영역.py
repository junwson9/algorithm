from collections import deque
def bfs(si,sj,h):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1
    while q:
        t = q.popleft()
        for di,dj in ((1,0), (0,1), (-1,0), (0,-1)):
            ni, nj = t[0]+di, t[1]+dj
            if (0<=ni<N and 0<=nj<N) and arr[ni][nj] > h:
                if v[ni][nj] == 0:
                    q.append((ni,nj))
                    v[ni][nj] = 1
    return 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mn = 100
mx = 0
ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > mx:
            mx = arr[i][j]


for h in range(mx):
    cnt = 0
    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and v[i][j] == 0:
                cnt += bfs(i,j, h)
                if cnt > ans:
                    ans = cnt

print(ans)