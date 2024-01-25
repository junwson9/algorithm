import sys
input = sys.stdin.readline
N,M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
lst = sorted(list(set(lst)))
N = len(lst)
def dfs(n,tmp):
    if n == M:
        print(*tmp)
        return

    for i in range(N):
        tmp.append(lst[i])
        dfs(n+1,tmp)
        tmp.pop()
dfs(0,[])