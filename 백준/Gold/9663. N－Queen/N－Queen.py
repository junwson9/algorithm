def dfs(n):
    global cnt
    if n == N:
        cnt += 1
        return

    for j in range(N):
        if v1[j] == 0 and v2[n+j] == 0 and v3[n-j] == 0:
            v1[j]=v2[n+j]=v3[n-j]=1
            dfs(n+1)
            v1[j]=v2[n+j]=v3[n-j]=0



N = int(input())
v1,v2,v3 = [[0]*(2*N+1) for _ in range(3)]
cnt = 0
dfs(0)
print(cnt)