def dfs(si,sj,flag):
    global ans
    ans = max(ans, v[si][sj])
    for di,dj in ((1,0),(0,1),(0,-1),(-1,0)):
        ni, nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<N:
            if arr[si][sj] > arr[ni][nj] and v[ni][nj] == 0:
                v[ni][nj] = v[si][sj] + 1
                dfs(ni,nj,flag)
                v[ni][nj] = 0
            elif flag == 1 and arr[si][sj] > arr[ni][nj]-K and v[ni][nj] == 0:
                tmp = arr[ni][nj]
                arr[ni][nj] = arr[si][sj]-1
                v[ni][nj] = v[si][sj] + 1
                dfs(ni,nj,flag-1)
                v[ni][nj] = 0
                arr[ni][nj] = tmp
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    ans = 0
    v = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > mx:
                mx = arr[i][j]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == mx:
                v[i][j] = 1
                dfs(i,j,1)
                v[i][j] = 0
    print(f'#{tc} {ans}')