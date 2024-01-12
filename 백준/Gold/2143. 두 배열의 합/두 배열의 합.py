import sys
from collections import defaultdict
input = sys.stdin.readline
T = int(input())
n = int(input())
a_lst = list(map(int, input().split()))
m = int(input())
b_lst = list(map(int, input().split()))
A_sum = defaultdict(int)
B_sum = defaultdict(int)

for i in range(n):
    for j in range(i,n):
        A_sum[sum(a_lst[i:j+1])] += 1
for i in range(m):
    for j in range(i,m):
        B_sum[sum(b_lst[i:j+1])] += 1
ans = 0

for key in A_sum.keys():
    ans += B_sum[T-key]*A_sum[key]
print(ans)