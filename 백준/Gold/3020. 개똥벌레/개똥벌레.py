import sys
input = sys.stdin.readline
N,H = map(int, input().split())
prefix = [0]*(H+1)
for i in range(1, N+1):
    suk = int(input())
    if i % 2 == 1:
        prefix[0] += 1
        prefix[suk] -= 1
    else:
        prefix[H] -= 1
        prefix[H-suk] += 1

for i in range(H):
    prefix[i+1] += prefix[i]
prefix = prefix[:-1]
count = 0
low = min(prefix)
for i in prefix:
    if i == low:
        count += 1

print(low, count)