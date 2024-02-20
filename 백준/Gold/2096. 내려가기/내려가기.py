import sys
input = sys.stdin.readline
N = int(input())
dp1 = [0]*3
dp2 = [0]*3

for _ in range(N):
    a,b,c = map(int,input().split())
    dp1 = [a+max(dp1[0],dp1[1]),b+max(dp1),c+max(dp1[1],dp1[2])]
    dp2 = [a+min(dp2[0],dp2[1]),b+min(dp2),c+min(dp2[1],dp2[2])]
print(max(dp1),min(dp2))