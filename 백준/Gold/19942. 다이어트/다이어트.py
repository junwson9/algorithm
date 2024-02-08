import sys
input = sys.stdin.readline
N = int(input())
mp,mf,ms,mv = map(int,input().split())
arr = [list(map(int ,input().split())) for _ in range(N)]
tmp = []
ans = []
def dfs(n,p,f,s,v,price,idx):
    global ans,ans2
    if n == N:
        if p >= mp and f >= mf and s >= ms and v >= mv:
            ans.append([price,tmp[:]])

        return

    for i in range(idx,N):
        tmp.append(i+1)
        dfs(n+1,p+arr[i][0],f+arr[i][1],s+arr[i][2],v+arr[i][3],price+arr[i][4],i+1)
        tmp.pop()
        dfs(n+1,p,f,s,v,price,i+1)


dfs(0,0,0,0,0,0,0)
if len(ans) == 0:
    print(-1)
else:
    ans.sort(key=lambda x:(x[0],x[1]))
    print(ans[0][0])
    print(*ans[0][1])
