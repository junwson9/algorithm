def spread():
    tmp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if (i == air_top and j == 0) or (i == air_btm and j == 0):
                continue
            if arr[i][j] > 0:
                for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
                    ni,nj = i+di,j+dj
                    if 0<=ni<R and 0<=nj<C and not ((ni == air_top and nj == 0) or (ni == air_btm and nj == 0)):
                        tmp[i][j] -= arr[i][j]//5
                        tmp[ni][nj] += arr[i][j]//5
    for i in range(R):
        for j in range(C):
            if (i == air_top and j == 0) or (i == air_btm and j == 0):
                continue
            else:
                arr[i][j] += tmp[i][j]

def move_top():
    ci,cj = air_top,2
    cur = arr[ci][cj]
    dr = 0
    while True:
        ni,nj = ci+di[dr],cj+dj[dr]
        if ni == air_top and nj == 0:
            break
        if 0<=ni<R and 0<=nj<C:
            tmp = arr[ni][nj]
            arr[ni][nj] = cur
            ci,cj = ni,nj
            cur = tmp
        else:
            dr += 1
    arr[air_top][2] = arr[air_top][1]
    arr[air_top][1] = 0

def move_down():
    ci,cj = air_btm,2
    cur = arr[ci][cj]
    dr = 4
    while True:
        ni,nj = ci+di[dr],cj+dj[dr]
        if ni == air_btm and nj == 0:
            break
        if 0<=ni<R and 0<=nj<C:
            tmp = arr[ni][nj]
            arr[ni][nj] = cur
            ci,cj = ni,nj
            cur = tmp
        else:
            dr += 1
    arr[air_btm][2] = arr[air_btm][1]
    arr[air_btm][1] = 0


import sys
input = sys.stdin.readline
R,C,T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
air_top = 0
for i in range(R):
    if arr[i][0] == -1:
        air_top = i
        break
air_btm = air_top+1
di = [0,-1,0,1,0,1,0,-1]
dj = [1,0,-1,0,1,0,-1,0]

for _ in range(T):
    spread()
    move_top()
    move_down()
ans = 0
for lst in arr:
    ans += sum(lst)
print(ans+2)