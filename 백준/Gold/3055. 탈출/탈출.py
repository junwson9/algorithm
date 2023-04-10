from collections import deque
def bfs():
    q = deque()
    ei = ej = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'S':
                q.append((i,j))
            if arr[i][j] == 'D':
                ei,ej = i,j

    for i in range(R):
        for j in range(C):
            if arr[i][j] == '*':
                q.append((i,j))

    while q:
        if arr[ei][ej] =='S':
            return v[ei][ej]
        t = q.popleft()
        for di,dj in ((1,0), (0,1), (-1,0), (0,-1)):
            ni, nj = t[0]+di, t[1]+dj
            if 0<=ni<R and 0<=nj<C:
                if arr[t[0]][t[1]] =='S' and (arr[ni][nj] == '.' or arr[ni][nj] == 'D'):
                    arr[ni][nj] = 'S'
                    q.append((ni,nj))
                    v[ni][nj] = v[t[0]][t[1]]+1
                if arr[t[0]][t[1]] =='*' and (arr[ni][nj] == '.' or arr[ni][nj] == 'S'):
                    arr[ni][nj] = '*'
                    q.append((ni,nj))
    return 'KAKTUS'




R,C = map(int, input().split())
v = [[0]*C for _ in range(R)]
arr = [list(input()) for _ in range(R)]
print(bfs())