from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    while q:
        t = q.popleft()
        for di,dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni, nj = t[0]+di, t[1]+dj
            if 0<= ni < N and 0<= nj < N:
                if v[ni][nj] > v[t[0]][t[1]]+arr[ni][nj]:
                    v[ni][nj] = v[t[0]][t[1]]+arr[ni][nj]
                    q.append((ni,nj))




tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    inf = N*N*10
    v = [[inf]*N for _ in range(N)]
    v[0][0] = arr[0][0]
    bfs(0,0)
    print(f'Problem {tc}: {v[-1][-1]}')