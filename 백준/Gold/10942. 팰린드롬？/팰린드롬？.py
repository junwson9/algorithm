import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
M = int(input())

dp = [[0]*N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if lst[i] == lst[i+1]:
        dp[i][i+1] = 1

for l in range(3,N+1):
    for s in range(N-l+1):
        e = s+l-1
        if lst[s] == lst[e] and dp[s+1][e-1]:
            dp[s][e] = 1


for _ in range(M):
    s,e = list(map(int,input().split()))
    print(dp[s-1][e-1])
