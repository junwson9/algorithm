import sys
input = sys.stdin.readline
N = int(input())
dp = [9999999999999]*(N+1)
dp[N] = 0
for total in range(N-1,-1,-1):
    for i in range(int(N**0.5),0,-1):
        if total+i**2 <= N:
            dp[total] = min(dp[total], dp[total+i**2]+1)
print(dp[0])

