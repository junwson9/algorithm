import sys
input = sys.stdin.readline

N,K = map(int,input().split())
first = [0]+list(map(int,input().split()))
sec = [0]+list(map(int, input().split()))

prefix1 = [0]*(N+1)
prefix2 = [0]*(N+1)
for i in range(1,N+1):
    prefix1[i] = prefix1[i-1]+first[i]
    prefix2[i] = prefix2[i-1]+sec[i]


idx1 = idx2 = N
while K:
    if prefix1[idx1] >= prefix2[idx2]:
        idx1 -= 1
    elif prefix1[idx1] < prefix2[idx2]:
        idx2 -= 1
    K -= 1

print(max(prefix1[idx1],prefix2[idx2]))