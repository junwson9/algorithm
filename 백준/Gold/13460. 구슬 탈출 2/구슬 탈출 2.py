import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(input().strip()) for _ in range(n)]
q = deque()
ri = rj = bi = bj  = 0
v = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            ri = i
            rj = j
        if arr[i][j] == 'B':
            bi = i
            bj = j

def move(x,y,dx,dy):
    move_cnt = 0
    while True:
        if arr[x+dx][y+dy] == '#' or arr[x][y] == 'O':
            break
        x += dx
        y += dy
        move_cnt += 1
    return x,y,move_cnt


def bfs():
    q = deque()
    q.append((ri,rj,bi,bj,1))
    v.append((ri,rj,bi,bj))
    while q:
        rx,ry,bx,by,cnt = q.popleft()
        if cnt > 10:
            break

        for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
            nrx,nry,rcnt = move(rx,ry,dx,dy)
            nbx,nby,bcnt = move(bx,by,dx,dy)

            if arr[nbx][nby] == 'O':
                continue

            if arr[nrx][nry] == 'O':
                print(cnt)
                return

            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if (nrx,nry,nbx,nby) not in v:
                v.append((nrx,nry,nbx,nby))
                q.append((nrx,nry,nbx,nby,cnt+1))

    print(-1)
bfs()






