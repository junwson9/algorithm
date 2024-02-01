import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
v = [0]*N
tmp = []
ans = 0
def dfs(n):
    global ans
    if n == N:
        sm = 0
        for i in range(1,N):
            sm += abs(tmp[i-1]-tmp[i])
        if sm > ans:
            ans = sm
        return

    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            tmp.append(lst[i])
            dfs(n+1)
            v[i] = 0
            tmp.pop()
dfs(0)
print(ans)
