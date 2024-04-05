import sys
from collections import deque
input = sys.stdin.readline
r,c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
ans = []
def bfs():
    q = deque()
    q.append((0,0))
    v[0][0] = 1
    cnt = 0
    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = ci+di,cj+dj
            if ni < 0 or ni >= r or nj < 0 or nj >= c:
                continue
            if v[ni][nj] == 1:
                continue
            if arr[ni][nj] == 0:
                v[ni][nj] = 1
                q.append((ni,nj))
            elif arr[ni][nj] == 1:
                arr[ni][nj] = 0
                v[ni][nj] = 1
                cnt += 1
    ans.append(cnt)
    return cnt

t = 0
while True:
    v = [[0]*c for _ in range(r)]
    cnt = bfs()
    if cnt == 0:
        break
    t += 1
print(t)
print(ans[-2])


