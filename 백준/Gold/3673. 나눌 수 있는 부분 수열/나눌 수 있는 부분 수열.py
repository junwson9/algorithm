import sys
from collections import defaultdict
input = sys.stdin.readline
c = int(input())
for _ in range(c):
    d, n = map(int, input().split())
    lst = list(map(int, input().split()))
    prefix_sum = [0]*(n+1)
    tmp = defaultdict(int)
    ans = 0
    for i in range(1,n+1):
        prefix_sum[i] = (prefix_sum[i-1]+lst[i-1])%d
    for i in range(n+1):
        tmp[prefix_sum[i]] += 1
    for key in tmp.keys():
        if tmp[key] >= 2:
            ans += tmp[key]*(tmp[key]-1)//2
    print(ans)


