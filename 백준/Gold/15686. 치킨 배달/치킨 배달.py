import sys
input = sys.stdin.readline
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chk = []
home = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chk.append((i,j))
        if arr[i][j] == 1:
            home.append((i,j))


tmp = []
def check(tmp):
    sm = 0
    for i,j in home:
        mn = N*N
        for ci,cj in tmp:
            if abs(i-ci)+abs(j-cj) < mn:
                mn = abs(i-ci)+abs(j-cj)
        sm += mn
    return sm

ans = 1e9
def dfs(n,idx):
    global ans
    if n == M:
        if check(tmp) < ans:
            ans = check(tmp)
        return

    for i in range(idx,len(chk)):
        tmp.append(chk[i])
        dfs(n+1,i+1)
        tmp.pop()
dfs(0,0)
print(ans)