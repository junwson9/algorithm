import sys
from collections import deque

input = sys.stdin.readline
def bfs(si,sj):
    q = deque()
    q.append([si,sj])
    while q:
        ci,cj = q.popleft()
        if ci == N-1 and cj == M-1:
            return
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0 > ni or ni >= N or 0 > nj or nj >= M:
                continue
            if arr[ni][nj] == 0:
                continue
            if v[ni][nj] < v[ci][cj]+1:
                q.append([ni,nj])
                v[ni][nj] = v[ci][cj]+1




N,M = map(int,input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

v[0][0] = 1
bfs(0,0)
print(v[N-1][M-1])
