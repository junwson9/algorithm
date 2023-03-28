def dfs(n,i,j,st):
    global ans
    if n == 6:
        ans.append(st)
        return

    for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
        ni, nj = i+di, j+dj
        if 0<= ni <4 and 0<= nj < 4:
            dfs(n+1,ni,nj,st+str(arr[ni][nj]))



T = int(input())
for tc in range(1, T+1):
    ans = []
    arr = [list(map(int, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            dfs(0,i,j,str(arr[i][j]))
    my_set = set(ans)
    print(f'#{tc} {len(my_set)}')