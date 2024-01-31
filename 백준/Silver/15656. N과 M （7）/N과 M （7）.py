import sys
input = sys.stdin.readline
N,M = map(int, input().split())
lst = sorted(list(map(int,input().split())))
tmp = []
def dfs(n):
    if n == M:
        print(*tmp)
        return
    for i in range(N):
        tmp.append(lst[i])
        dfs(n+1)
        tmp.pop()
dfs(0)



