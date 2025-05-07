import sys

input = sys.stdin.readline
N,K = map(int,input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
ans = 0
for i in range(N):
    if K//lst[i]:
        ans += K//lst[i]
        K = K%lst[i]
print(ans)