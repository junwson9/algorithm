import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = list(map(int, input().split()))
sm = sum(lst[:k])
ans = [sm]
for i in range(n-k):
    sm = sm - lst[i] + lst[i+k]
    ans.append(sm)
print(max(ans))