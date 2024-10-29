import sys

input = sys.stdin.readline
H,W,N,M = map(int,input().split())
ans = 0
for x in range(1,H+1,N+1):
    for y in range(1,W+1,M+1):
        ans += 1

print(ans)

