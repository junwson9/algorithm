import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
r,c = map(int,input().split())
arr = [list(input().strip()) for _ in range(r)]
v = [[0]*c for _ in range(r)]

def dfs(i,j):
    v[i][j] = 1
    if j == c-1:
        return True
    for di,dj in ((-1,1),(0,1),(1,1)):
        ni,nj = i+di,j+dj
        if 0<=ni<r and 0<=nj<c:
            if not v[ni][nj] and arr[ni][nj] != 'x':
                if dfs(ni,nj):
                    return True
    return False

ans = 0
for i in range(r):
    if dfs(i,0):
        ans += 1
print(ans)