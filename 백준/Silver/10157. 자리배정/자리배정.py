C, R = map(int, input().split())
K = int(input())
v = [[0]*C for _ in range(R)]
arr = [[0]*C for _ in range(R)]
di = [-1,0,1,0]
dj = [0,1,0,-1]
cnt = 1
dr = 0
ci,cj = R-1, 0
v[ci][cj] = 1
while True:
    arr[ci][cj] = cnt
    ni,nj = ci+di[dr], cj+dj[dr]
    if (0<=ni<R and 0<=nj<C) and v[ni][nj] == 0:
        v[ni][nj] = 1
        ci,cj = ni,nj
    else:
        dr = (dr+1)%4
        ni,nj = ci+di[dr],cj+dj[dr]
        v[ni][nj] = 1
        ci,cj = ni,nj
    cnt += 1
    if cnt == R*C+1:
        break

rlt = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == K:
            rlt.append(j+1)
            rlt.append(R-i)

if len(rlt):
    print(*rlt)
else:
    print(0)