import sys
input = sys.stdin.readline
T = int(input())
def gcd(a,b):
    while b > 0:
        a,b = b,a%b
    return a
dp = [0] * 1001
dp[1] = 3
for i in range(2,1001):
    cnt = 0
    for j in range(1,i):

        if gcd(i,j) == 1:
            cnt += 2
    dp[i] = dp[i-1]+cnt
for _ in range(T):
    N = int(input())
    print(dp[N])
