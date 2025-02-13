T = int(input())

for _ in range(T):
    K = int(input())
    lst = [0]+list(map(int,input().split()))
    dp = [[-1]*K for _ in range(K)]

    prefix = [0]*(K+1)
    for i in range(1,K+1):
        prefix[i] = prefix[i-1]+lst[i]



    def dfs(s,e):
        if s == e:
            return 0

        if dp[s][e] != -1:
            return dp[s][e]

        ans = 1e9
        for mid in range(s,e):
            ans = min(dfs(s,mid)+dfs(mid+1,e)+(prefix[e+1]-prefix[s]),ans)
        dp[s][e] = ans
        return dp[s][e]



    dfs(0,K-1)
    print(dp[0][K-1])

