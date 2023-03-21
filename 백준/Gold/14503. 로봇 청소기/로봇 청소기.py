N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
di = [-1, 0, 1, 0]  #북동남서
dj = [0, 1, 0 , -1]
ci, cj = r, c
cnt = 1
while True:
    flag = 1
    v[ci][cj] = 1
    for _ in range(4):
        d = (d+3)%4
        ni, nj = ci+di[d], cj+dj[d]
        if (0<= ni < N and 0<= nj < M) and arr[ni][nj] == 0:
            if v[ni][nj] == 0:
                cnt += 1
                ci, cj = ni, nj
                flag = 0
                break
    if flag == 1:
        ni, nj = ci-di[d], cj-dj[d]
        if arr[ni][nj] == 1:
            print(cnt)
            break
        else:
            ci, cj = ni, nj