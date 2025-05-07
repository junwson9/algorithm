import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def bfs(si,sj):
    visited[si][sj] = 1
    q = deque()
    q.append([si,sj])
    while q:
        ci,cj = q.popleft()
        for di,dj in((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<n and 0<=nj<m:
                if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[ci][cj]+1
                    q.append([ni,nj])

bfs(0,0)
print(visited[n-1][m-1])
