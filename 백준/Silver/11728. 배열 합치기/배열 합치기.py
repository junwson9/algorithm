import sys
input = sys.stdin.readline
N,M = map(int, input().split())
InF = 1e9+1
A = list(map(int, input().split())) + [InF]*M
B = list(map(int ,input().split())) + [InF]*N
s1 = 0
s2 = 0
ans = []
while True:
    if A[s1] == InF and B[s2] == InF:
        break
    if A[s1] > B[s2]:
        ans.append(B[s2])
        s2 += 1
    elif A[s1] < B[s2]:
        ans.append(A[s1])
        s1 += 1
    else:
        ans.append(A[s1])
        ans.append(B[s2])
        s1 += 1
        s2 += 1
print(*ans)