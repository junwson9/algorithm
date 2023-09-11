import sys
input = sys.stdin.readline
N,M = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(N)]
csum = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        csum[i][j] = csum[i-1][j]+csum[i][j-1]-csum[i-1][j-1]+arr[i-1][j-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    result = csum[x2][y2]-csum[x2][y1-1]-csum[x1-1][y2]+csum[x1-1][y1-1]
    print(result)


