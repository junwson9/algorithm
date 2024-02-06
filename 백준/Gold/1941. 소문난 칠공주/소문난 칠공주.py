import sys
from collections import deque
input = sys.stdin.readline
arr = [list(input().strip()) for _ in range(5)]
ans = 0
def bfs(tmp):
    v = [[1]*5 for _ in range(5)]
    for si,sj in tmp:
        v[si][sj] = 0
    q = deque()
    q.append(tmp[0])
    v[tmp[0][0]][tmp[0][1]] = 1
    check = 1
    while q:
        t = q.popleft()
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = t[0]+di,t[1]+dj
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj] == 0:
                v[ni][nj] = 1
                check += 1
                q.append((ni,nj))
    if check != 7:
        return False
    else:
        return True
tmp = []
def dfs(n,s,y_cnt):
    global ans
    if y_cnt > 3:
        return
    if n == 7:
        if bfs(tmp):
            ans += 1
        return

    for i in range(s,25):
        r = i//5
        c = i%5
        tmp.append((r,c))
        if arr[r][c] == 'Y':
            dfs(n+1,i+1,y_cnt+1)
        else:
            dfs(n+1,i+1,y_cnt)
        tmp.pop()
dfs(0,0,0)
print(ans)

