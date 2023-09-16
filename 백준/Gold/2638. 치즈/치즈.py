import sys
from collections import deque
def bfs():
    v = [[0] * M for _ in range(N)]
    q = deque()
    q.append((0,0))
    v[0][0] = 1
    while q:
        t = q.popleft()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = t[0]+di, t[1]+dj
            if 0<= ni < N and 0<= nj < M:
                if v[ni][nj] == 0:
                    if arr[ni][nj] == 0:
                        q.append((ni,nj))
                        v[ni][nj] = 1
                    else:
                        v[ni][nj] = v[t[0]][t[1]]+1

    lst = []
    for i in range(N):
        for j in range(M):
            if v[i][j] == 2:
                cnt = 0
                for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
                    ni,nj = i+di,j+dj
                    if 0<= ni < N and 0<= nj < M:
                        if v[ni][nj] == 1:
                            cnt += 1
                if cnt >= 2:
                    lst.append((i,j))
    return lst



input = sys.stdin.readline
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    lst = bfs()
    if len(lst) == 0:
        break
    ans += 1
    for x,y in lst:
        arr[x][y] = 0
print(ans)
