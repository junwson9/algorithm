import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))
lst.sort()
tmp = set()
def dfs(n,sm):
    if n == N:
        tmp.add(sm)
        return

    dfs(n+1,sm+lst[n])
    dfs(n+1,sm)

dfs(0,0)
InF = int(1e9)
ans = 0
for i in range(1,InF):
    if i in tmp:
        continue
    else:
        ans = i
        break

print(ans)