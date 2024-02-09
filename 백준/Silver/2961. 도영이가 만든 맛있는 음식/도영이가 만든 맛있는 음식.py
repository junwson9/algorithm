import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 1e9
tmp = []
def dfs(n,s,b,idx):
    global ans
    if n == N:
        if abs(s-b) < ans and len(tmp) > 0:
            ans = abs(s-b)
        return

    for i in range(idx,N):
        tmp.append(i)
        dfs(n+1,s*arr[i][0],b+arr[i][1],i+1)
        tmp.pop()
        dfs(n+1,s,b,i+1)

dfs(0,1,0,0)
print(ans)