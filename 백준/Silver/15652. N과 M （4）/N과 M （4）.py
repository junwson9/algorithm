import sys

input = sys.stdin.readline
N,M = map(int,input().split())
tmp = []

def dfs(n,idx):
    if n == M:
        print(*tmp)
        return

    for i in range(idx,N+1):
        tmp.append(i)
        dfs(n+1,i)
        tmp.pop()
dfs(0,1)


