import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N = int(input())
arr = [list(map(int,input().strip())) for _ in range(N)]
v = [[False]*N for _ in range(N)]
def dfs(ci,cj):
    global tmp
    v[ci][cj] = True
    tmp += 1
    for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
        ni,nj = ci+di,cj+dj
        if 0<=ni<N and 0<=nj<N:
            if not v[ni][nj] and arr[ni][nj]:
                dfs(ni,nj)
    return tmp


cnt = 0
rlt = []
for i in range(N):
    for j in range(N):
        if not v[i][j] and arr[i][j]:
            tmp = 0
            rlt.append(dfs(i,j))
            cnt += 1
rlt.sort()
print(cnt)
for n in rlt:
    print(n)
