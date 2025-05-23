import sys

input = sys.stdin.readline
N,M = map(int,input().split())
tmp = []
v = [0]*(N+1)
def dfs(n):
    if n == M:
        print(*tmp)
        return

    for i in range(1,N+1):
        if not v[i]:
            v[i] = 1
            tmp.append(i)
            dfs(n+1)
            v[i] = 0
            tmp.pop()
dfs(0)


