import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [list(map(int,input().strip())) for _ in range(n)]
v = [[[0]*2 for _ in range(m)] for _ in range(n)]
def bfs(i,j,k):
    q = deque()
    q.append((i,j,k))
    v[0][0][0] = 1
    while q:
        x,y,c = q.popleft()
        if x == n-1 and y == m-1:
            return v[x][y][c]
        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx,ny = x+dx,y+dy
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if arr[nx][ny] == 1 and c == 0:
                v[nx][ny][1] = v[x][y][0]+1
                q.append((nx,ny,1))
            elif arr[nx][ny] == 0 and v[nx][ny][c] == 0:
                v[nx][ny][c] = v[x][y][c]+1
                q.append((nx,ny,c))
    return -1
print(bfs(0,0,0))
