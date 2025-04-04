import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
lst = list(map(int,input().split()))
lst.sort()
dist = []
for i in range(N-1):
    dist.append(lst[i+1]-lst[i])

dist.sort()
print(sum(dist[:N-K]))