import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)
lst = [0]*(N+1)
for i in range(2,N+1):
    dp[i] = dp[i-1]+1
    lst[i] = i-1
    if i%3 == 0 and dp[i] > dp[i//3]+1:
        dp[i] = dp[i//3] + 1
        lst[i] = i//3
    if i%2 == 0 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i // 2] + 1
        lst[i] = i//2


print(dp[N])
print(N, end=" ")
n = N
while True:
    if n == 1:
        break
    print(lst[n], end=" ")
    n = lst[n]
