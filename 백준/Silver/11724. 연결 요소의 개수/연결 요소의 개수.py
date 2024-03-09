import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N,M = map(int,input().split())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int, input().split())
    adjL[x].append(y)
    adjL[y].append(x)
v = [False]*(N+1)
def dfs(n):
    v[n] = True
    for i in adjL[n]:
        if v[i]:
            continue
        dfs(i)
cnt = 0
for i in range(1,N+1):
    if v[i]:
        continue
    dfs(i)
    cnt += 1
print(cnt)




