import sys

input = sys.stdin.readline
N,K = map(int, input().split())
lst = list(map(int, input().split()))
prefix = [0]*(N-K+1)
prefix[0] = sum(lst[:K])

for i in range(1,N-K+1):
    prefix[i] = prefix[i-1] + lst[i+K-1] - lst[i-1]
print(max(prefix))

