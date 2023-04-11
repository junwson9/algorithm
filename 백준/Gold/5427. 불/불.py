from collections import deque
def bfs():
    q = deque()
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                v[i][j] = '0'
                q.append((i,j))
            if arr[i][j] == '#':
                v[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                v[i][j] = '*'
                q.append((i,j))

    while q:
        ci, cj = q.popleft()
        if ci == h-1 or ci == 0 or cj == w-1 or cj == 0:
            if v[ci][cj].isdigit():
                return int(v[ci][cj])+1
        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<h and 0<=nj<w:
                if v[ni][nj] == '.' and v[ci][cj].isdigit():
                    v[ni][nj] = str(int(v[ci][cj])+1)
                    q.append((ni,nj))

                elif (v[ni][nj] == '.' or v[ni][nj].isdigit()) and v[ci][cj] =='*':
                    v[ni][nj] = '*'
                    q.append((ni,nj))
    return 'IMPOSSIBLE'




T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    v = [['.']*w for _ in range(h)]
    print(bfs())
