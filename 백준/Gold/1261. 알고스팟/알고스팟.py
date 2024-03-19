import sys
from collections import deque
input = sys.stdin.readline
M,N = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(N)]
dist = [[-1]*M for _ in range(N)]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    dist[i][j] = 0
    while q:
        t = q.popleft()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = t[0]+di,t[1]+dj
            if 0<= ni < N and 0<= nj < M:
                if dist[ni][nj] == -1:
                    if arr[ni][nj] == 0:
                        dist[ni][nj] = dist[t[0]][t[1]]
                        q.appendleft((ni,nj))
                    if arr[ni][nj] == 1:
                        dist[ni][nj] = dist[t[0]][t[1]]+1
                        q.append((ni, nj))



bfs(0,0)
print(dist[-1][-1])
