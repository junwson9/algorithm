from collections import deque
def bfs(i,j):
    global ans
    q = deque()
    q.append((i,j))
    while q:
        ci,cj = q.popleft()
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni, nj = ci+di, cj+dj
            if (0<=ni<N and 0<=nj<M) and arr[ni][nj] == 1:
                if v[ni][nj] == 0:
                    q.append((ni,nj))
                    v[ni][nj] = 1
    ans += 1


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    v = [[0]*M for _ in range(N)]
    arr = [[0]*M for _ in range(N)]
    ans = 0
    for _ in range(K):
        j,i = map(int, input().split())
        arr[i][j] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and v[i][j] == 0:
                bfs(i,j)
    print(ans)