import sys
from collections import deque

input = sys.stdin.readline
M,N = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(M)]
v = [[0]*N for _ in range(M)]
answer = 'NO'
def bfs(i,j):
    q = deque()
    q.append([i,j])
    v[i][j] = 1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<= ni < M and 0<= nj <N:
                if arr[ni][nj] != 1 and v[ni][nj] == 0:
                    q.append([ni,nj])
                    v[ni][nj] = 1



for j in range(N):
    if arr[0][j] == 0:
        bfs(0,j)


for j in range(N):
    if v[M-1][j] == 1:
        answer = 'YES'
        
print(answer)



