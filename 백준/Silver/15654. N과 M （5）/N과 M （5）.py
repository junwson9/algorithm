import sys
input = sys.stdin.readline
N,M = map(int, input().split())
lst = sorted(list(map(int,input().split())))
tmp = []
v = [0]*N
def dfs(n):
    if n == M:
        print(*tmp)
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            tmp.append(lst[i])
            dfs(n+1)
            v[i] = 0
            tmp.pop()
dfs(0)



