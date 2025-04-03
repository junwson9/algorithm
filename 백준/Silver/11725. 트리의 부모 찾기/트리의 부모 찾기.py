import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
adjL = [[] for _ in range(n+1)]
parent = [0]*(n+1)
for _ in range(n-1):
    s,e = map(int,input().split())
    adjL[s].append(e)
    adjL[e].append(s)

def dfs(cur,prev):
    for nxt in adjL[cur]:
        if nxt == prev:
            continue
        parent[nxt] = cur
        dfs(nxt,cur)

dfs(1,0)
for i in range(2,n+1):
    print(parent[i])