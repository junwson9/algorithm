import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N = int(input())
arr = [list(input()) for _ in range(N)]
v = [[False]*N for _ in range(N)]
di = [1,0,-1,0]
dj = [0,1,0,-1]

def dfs(ci,cj):
    global cnt
    v[ci][cj] = True
    cnt += 1
    for k in range(4):
        ni = ci+di[k]
        nj = cj+dj[k]
        if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ni][nj] == '1':
            dfs(ni,nj)

    return cnt
rlt = 0
lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not v[i][j]:
            cnt = 0
            lst.append(dfs(i,j))
            rlt += 1
print(rlt)
lst.sort()
for n in lst:
    print(n)
