import sys

input = sys.stdin.readline

N,M = map(int,input().split())
h = list(map(int,input().split()))

imos = [0]*(N+1)

for _ in range(M):
    a,b,k = map(int,input().split())
    imos[a-1] += k
    imos[b] -= k

for i in range(1,len(imos)):
    imos[i] = imos[i-1]+imos[i]


for i in range(N):
    print(h[i]+imos[i], end=' ')



