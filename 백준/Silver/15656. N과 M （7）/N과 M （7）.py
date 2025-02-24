import sys

input = sys.stdin.readline

N,M = map(int,input().split())
lst = sorted(list(map(int,input().split())))

def dfs(n,tmp):
    if n == M:
        print(*tmp)
        return

    for i in range(N):
        dfs(n+1,tmp+[lst[i]])

dfs(0,[])
