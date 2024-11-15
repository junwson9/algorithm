import sys

input = sys.stdin.readline

N,L,R,X = map(int,input().split())
lst = list(map(int,input().split()))
solve = []
v = [0]*N
ans = 0
def dfs(n,solve):
    global ans
    if n == N:
        if len(solve) >= 2:
            if abs(max(solve)-min(solve)) >= X and L<= sum(solve) <= R:
                ans += 1
        return

    dfs(n+1,solve+[lst[n]])
    dfs(n+1,solve)

dfs(0,[])
print(ans)




















