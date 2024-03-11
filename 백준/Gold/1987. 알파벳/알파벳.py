import sys
input = sys.stdin.readline
R,C = map(int,input().split())
arr = [list(input().strip()) for _ in range(R)]
ans = 0
di = [-1,1,0,0]
dj = [0,0,-1,1]
def dfs(ci,cj,cnt):
    global ans
    ans = max(cnt,ans)
    for i in range(4):
        ni = ci+di[i]
        nj = cj+dj[i]
        if 0 <= ni < R and 0 <= nj < C and not arr[ni][nj] in v:
            v.add(arr[ni][nj])
            dfs(ni,nj,cnt + 1)
            v.remove(arr[ni][nj])

v = set()
v.add(arr[0][0])
dfs(0,0,1)
print(ans)

