import sys

input = sys.stdin.readline

N,M = map(int,input().split())
lst = sorted(list(map(int,input().split())))

def dfs(n,idx,tmp):
    if n == M:
        print(*tmp)
        return

    for i in range(idx,N):
        dfs(n+1,i,tmp+[lst[i]])

dfs(0,0,[])
