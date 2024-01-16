import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
prefix_sum = [0]*(N+1)
suffix_sum = [0]*(N+1)
def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a
prefix_sum[0] = lst[0]
suffix_sum[N-1] = lst[N-1]
for i in range(1,N):
    prefix_sum[i] = gcd(prefix_sum[i-1],lst[i])
for j in range(N-2,-1,-1):
    suffix_sum[j] = gcd(suffix_sum[j+1],lst[j])
ans = [-1]
for i in range(N):
    l = prefix_sum[i-1]
    r = suffix_sum[i+1]
    tmp = gcd(l,r)
    if lst[i]%tmp == 0:
        continue
    ans= [tmp, lst[i]]
print(*ans)
