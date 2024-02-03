import sys
from collections import deque
input = sys.stdin.readline
while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break

    def bfs(si,sj):
        global ans
        q = deque()
        q.append((si,sj))
        v[si][sj] = 1
        while q:
            t = q.popleft()
            for di,dj in ((1,0),(0,1),(-1,0),(0,-1),(1,-1),(1,1),(-1,-1),(-1,1)):
                ci,cj = t[0]+di,t[1]+dj
                if 0<=ci<h and 0<=cj<w:
                    if v[ci][cj] == 0 and arr[ci][cj] == 1:
                        v[ci][cj] = 1
                        q.append((ci,cj))
        ans += 1



    arr = [list(map(int, input().split())) for _ in range(h)]
    v = [[0]*w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and v[i][j] == 0:
                bfs(i,j)
    print(ans)
