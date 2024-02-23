import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
dp = [1]*(N)
prev = [-1]*(N)
for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            if dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
                prev[i] = j

mx = -1
idx = 0
ans = []
for i in range(N):
    if mx < dp[i]:
        mx = dp[i]
        idx = i
while idx != -1:
    ans.append(lst[idx])
    idx = prev[idx]

print(max(dp))
print(*ans[::-1])
