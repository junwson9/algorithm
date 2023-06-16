N = int(input())
dp = [N]*(N+1)
dp[0] = 0
for i in range(3,N+1):
    if i//5 > 0:
        dp[i] = min(dp[i-5]+1,dp[i])
    if i//3 > 0:
        dp[i] = min(dp[i-3]+1,dp[i])
if dp[N] == N:
    print(-1)
else:
    print(dp[N])
