import sys

input = sys.stdin.readline

N,M = map(int,input().split())

def dfs(n,tmp):
    if n == M:
        print(*tmp)
        return

    for i in range(1,N+1):

        dfs(n+1,tmp+[i])

dfs(0,[])
