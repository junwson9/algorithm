import sys

input = sys.stdin.readline

N,M = map(int,input().split())
lst = sorted(list(map(int,input().split())))
v = [0]*N

def dfs(n,tmp):
    if n == M:
        print(*tmp)
        return

    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1,tmp+[lst[i]])
            v[i] = 0

dfs(0,[])
