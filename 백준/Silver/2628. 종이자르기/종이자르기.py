import sys
W, H = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
check = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
garo = [0]
sero = [0]
for i in range(N):
    if check[i][0] == 0:
        garo.append(check[i][1])
    else:
        sero.append(check[i][1])
garo.append(H)
sero.append(W)
garo.sort()
sero.sort()
max_garo = 0
max_sero = 0
for m in range(len(garo)-1):
    if garo[m+1]-garo[m] > max_garo:
        max_garo = garo[m+1]-garo[m]
for k in range(len(sero)-1):
    if sero[k+1]-sero[k] > max_sero:
        max_sero = sero[k+1]-sero[k]
print(f'{max_garo*max_sero}')