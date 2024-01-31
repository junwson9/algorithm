import sys
input = sys.stdin.readline
N,M = map(int, input().split())
lst = sorted(list(map(int,input().split())))
tmp = []
def dfs(n,idx):
    if n == M:
        print(*tmp)
        return
    for i in range(idx,N):
        tmp.append(lst[i])
        dfs(n+1,i+1)
        tmp.pop()
dfs(0,0)



