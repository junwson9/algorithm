import sys
from collections import deque
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
q = deque()
arr = [[0]*N for _ in range(N)]
dir = []
di = [0,-1,0,1]
dj = [1,0,-1,0]
for _ in range(K):
    r,c = map(int, sys.stdin.readline().split())
    arr[r-1][c-1] = 1
L = int(sys.stdin.readline())
for _ in range(L):
    x,c = sys.stdin.readline().split()
    dir.append((int(x),c))
dr = time = 0
i = j = 0
x = 0
q.append((0,0))
while True:
    i,j = i+di[dr],j+dj[dr]
    time += 1
    if 0>i or i>N-1 or j<0 or j>N-1 or (i,j) in q:
        break
    q.append((i,j))
    if arr[i][j] == 0:
        q.popleft()
    else:
        arr[i][j] = 0
    if time == dir[x][0]:
        if dir[x][1] == 'L':
            dr = (dr+1)%4
        if dir[x][1] == 'D':
            dr = (dr+3)%4
        if x+1 < len(dir):
            x += 1
print(time)
