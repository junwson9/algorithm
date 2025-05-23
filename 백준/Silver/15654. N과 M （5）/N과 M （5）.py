import sys

input = sys.stdin.readline
N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
tmp = []
v = [0]*N

def dfs(n):
    if n == M:
        print(*tmp)
        return

    for i in range(len(lst)):
        if not v[i]:
            v[i] = 1
            tmp.append(lst[i])
            dfs(n+1)
            tmp.pop()
            v[i] = 0
dfs(0)


