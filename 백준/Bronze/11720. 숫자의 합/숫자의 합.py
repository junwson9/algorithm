import sys

input = sys.stdin.readline
N = int(input())
S = list(input().strip())
ans = 0
for s in S:
    ans += int(s)
print(ans)




