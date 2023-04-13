N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
for i in range(1,N):
    D[i][0] = D[i][0]+min(D[i-1][1], D[i-1][2])
    D[i][1] = D[i][1]+min(D[i-1][0], D[i-1][2])
    D[i][2] = D[i][2]+min(D[i-1][0], D[i-1][1])
print(min(D[N-1]))