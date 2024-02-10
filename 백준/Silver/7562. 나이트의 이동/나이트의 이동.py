import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
def bfs(ci,cj):
    q = deque()
    q.append((ci,cj))
    v[ci][cj] = 0
    while q:
        t = q.popleft()
        for di,dj in ((2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)):
            ni,nj = t[0]+di,t[1]+dj
            if 0<=ni<N and 0<=nj<N:
                if v[t[0]][t[1]]+1 < v[ni][nj]:
                    v[ni][nj] = v[t[0]][t[1]]+1
                    q.append((ni,nj))



for _ in range(T):
    N = int(input())
    ci,cj = map(int, input().split())
    ei,ej = map(int, input().split())
    InF = int(1e9)
    v = [[InF]*N for _ in range(N)]
    bfs(ci,cj)
    if v[ei][ej] == InF:
        print(0)
    else:
        print(v[ei][ej])
