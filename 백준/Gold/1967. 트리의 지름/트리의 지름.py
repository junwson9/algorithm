import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def dfs(cur,cost):
    for nxt in graph[cur]:
        nxtv,nxtcost = nxt
        if d[nxtv] == -1:
            d[nxtv] = cost+nxtcost
            dfs(nxtv,cost+nxtcost)

d = [-1]*(n+1)
d[1] = 0
dfs(1,0)
mx = 0
mx_i = 0
for i in range(1,n+1):
    if d[i] > mx:
        mx = d[i]
        mx_i = i
d = [-1]*(n+1)
d[mx_i] = 0
dfs(mx_i,0)
print(max(d))