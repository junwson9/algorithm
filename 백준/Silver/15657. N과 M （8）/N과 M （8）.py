import sys

input = sys.stdin.readline
N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
tmp = []

def dfs(n,idx):
    if n == M:
        print(*tmp)
        return

    for i in range(idx,len(lst)):
        tmp.append(lst[i])
        dfs(n+1,i)
        tmp.pop()

dfs(0,0)


