import sys

input = sys.stdin.readline
N,K = map(int,input().split())
lst = list(map(int,input().split()))
r = [list(map(int,input().split())) for _ in range(K)]
m = [list(map(int,input().split())) for _ in range(K)]
ans = 0

def dfs(n,sm):
    global ans
    if n == K:
        if sm > ans:
            ans = sm
        return

    for i in range(N):
        if lst[i] > 0:
            lst[i] -= 1
        else:
            continue

        for j in range(N):
            if lst[j] > 0:
                lst[j] -= 1
                dfs(n+1,sm+r[n][i]+m[n][j])
            else:
                continue
            lst[j] += 1
        lst[i] += 1

dfs(0,0)
print(ans)

