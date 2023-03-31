def dfs(i,j,dr,cnt):
    global si, sj, ans
    if dr < 3:
        drdr = dr+2
    else:
        drdr = dr+1
    for d in range(dr, drdr):
        ni = i+dr_lst[d][0]
        nj = j+dr_lst[d][1]
        if si == ni and sj == nj:
            ans = max(ans,cnt)
            return
        if 0<=ni<N and 0<=nj<N:
            if v1[ni][nj] == 0 and v2[arr[ni][nj]] == 0:
                v1[ni][nj] = 1
                v2[arr[ni][nj]] = 1
                dfs(ni,nj,d,cnt+1)
                v1[ni][nj] = 0
                v2[arr[ni][nj]] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v1 = [[0]*N for _ in range(N)]
    v2 = [0]*101
    ans = -1
    dr_lst = [(1,1),(1,-1),(-1,-1),(-1,1)]
    for i in range(N):
        for j in range(N):
            si, sj = i, j
            v1[i][j] = 1
            v2[arr[i][j]] = 1
            dfs(i,j,0,1)
            v1[i][j] = 0
            v2[arr[i][j]] = 0
    print(f'#{tc} {ans}')
