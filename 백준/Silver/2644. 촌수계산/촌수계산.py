import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N = int(input())
s,e = map(int, input().split())
M = int(input())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int, input().split())
    adjL[x].append(y)
    adjL[y].append(x)
v = [False]*(N+1)
ans = []
def dfs(n,cnt):
    if n == e:
        ans.append(cnt)
        return
    v[n] = True
    for i in adjL[n]:
        if v[i]:
            continue
        dfs(i,cnt+1)


dfs(s,0)
if len(ans):
    print(*ans)
else:
    print(-1)




