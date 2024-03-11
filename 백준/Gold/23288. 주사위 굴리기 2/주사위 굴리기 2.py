import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dice = [1,2,3,4,5,6]
def move(dr,i,j):
    global dice
    # 동
    if dr == 0:
        dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]

    # 시계방향으로
    elif dr == 1:
        dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]

    elif dr == 2:
        dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    else:
        dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]

    if dice[5] > arr[i][j]:
        dr = (dr+1)%4
    if dice[5] < arr[i][j]:
        dr = (dr+3)%4
    return dr

def score(n,x,y):
    v = [[False]*M for _ in range(N)]
    q = deque()
    q.append((x,y))
    v[x][y] = True
    sm = 0
    while q:
        i,j = q.popleft()
        sm += n
        for k in range(4):
            ni,nj = i+di[k],j+dj[k]

            if 0<=ni<N and 0<=nj<M:
                if not v[ni][nj]:
                    if arr[ni][nj] == n:
                        q.append((ni,nj))
                        v[ni][nj] = True

    return sm


di = [0,1,0,-1]
dj = [1,0,-1,0]
dr = 0
i = j = 0
ans = 0
for _ in range(K):
    ni = i+di[dr]
    nj = j+dj[dr]
    if 0 > ni or ni >= N or 0 > nj or nj >= M:
        ni = i-di[dr]
        nj = j-dj[dr]
        dr = (dr+2)%4

    dr = move(dr,ni,nj)
    ans += score(arr[ni][nj],ni,nj)
    i,j = ni,nj
print(ans)
