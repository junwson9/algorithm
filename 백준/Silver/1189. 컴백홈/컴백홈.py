def dfs(i,j,k):
    global ans
    v[i][j] = 1
    if k == K:
        if i == 0 and j == C-1:
            ans += 1
            return

    for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
        ni,nj = i+di, j+dj
        if 0<= ni <R and 0<= nj <C and arr[ni][nj] == '.':
            if v[ni][nj] == 0:
                v[ni][nj] = 1
                dfs(ni,nj,k+1)
                v[ni][nj] = 0


R,C,K = map(int, input().split())
arr = [list(input()) for _ in range(R)]
v = [[0]*C for _ in range(R)]
ans = 0
dfs(R-1,0,1)
print(ans)