import sys
input = sys.stdin.readline
N,M = map(int, input().split())
lst = []
def dfs(n,idx):
    if n == M:
        print(*lst)
        return
    for i in range(idx,N+1):
            lst.append(i)
            dfs(n+1,i)
            lst.pop()
dfs(0,1)



