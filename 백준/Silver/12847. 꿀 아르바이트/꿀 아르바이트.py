import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [0]+list(map(int,input().split()))
prefix_sum = [0]*(n+1)

for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i-1]+lst[i]

rlt = 0
for i in range(m,n):
    rlt = max(rlt,prefix_sum[i]-prefix_sum[i-m])

print(rlt)