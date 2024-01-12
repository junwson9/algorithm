import sys
input = sys.stdin.readline
N = int(input())
mx = 0
mx_idx = 0
lst = [0]*1001
for _ in range(N):
    L,H = map(int, input().split())
    lst[L] = H
    if mx < H:
        mx_idx = L
        mx = H
left = right = 0
ans = 0
for i in range(mx_idx+1):
    left = max(left,lst[i])
    ans += left

for j in range(1000,mx_idx,-1):
    right = max(right,lst[j])
    ans += right
print(ans)