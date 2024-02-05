import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*N for _ in range(N)]
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1
    while q:
        t = q.popleft()
        mul = arr[t[0]][t[1]]
        for di,dj in ((1,0),(0,1)):
            ni,nj = t[0]+di*mul,t[1]+dj*mul
            if 0<=ni<N and 0<=nj<N:
                if v[ni][nj] == 0:
                    v[ni][nj] = 1
                    q.append((ni,nj))

bfs(0,0)
if v[N-1][N-1] == 1:
    print('HaruHaru')
else:
    print('Hing')


