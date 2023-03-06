T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = arr[i][j]
            for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                for k in range(1,M):
                    ni,nj = i+di*k, j+dj*k
                    if 0<= ni < N and 0<= nj < N:
                        ans += arr[ni][nj]
            if ans > mx:
                mx = ans
    for i in range(N):
        for j in range(N):
            ans = arr[i][j]
            for di, dj in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
                for k in range(1, M):
                    ni, nj = i + di * k, j + dj * k
                    if 0 <= ni < N and 0 <= nj < N:
                        ans += arr[ni][nj]
            if ans > mx:
                mx = ans
    print(f'#{tc} {mx}')

