import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
A = list(map(int ,input().split()))
B = list(map(int, input().split()))
sm = defaultdict(int)
sm[0] = 1
ans = 0
A_sum = B_sum = 0
for i in range(N):
    A_sum += A[i]
    B_sum += B[i]
    ans += sm[A_sum-B_sum]
    sm[A_sum-B_sum] += 1

print(ans)
