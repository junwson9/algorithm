import sys

input = sys.stdin.readline

N,M = map(int,input().split())
v = [0]*(N+1)

def dfs(n,tmp):
    if n == M:
        print(*tmp)
        return

    for i in range(1,N+1):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1,tmp+[i])
            v[i] = 0

dfs(0,[])
