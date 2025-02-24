import sys

input = sys.stdin.readline

N,M = map(int,input().split())

def dfs(n,idx,tmp):
    if n == M:
        print(*tmp)
        return

    for i in range(idx,N+1):
        dfs(n+1,i+1,tmp+[i])

dfs(0,1,[])
