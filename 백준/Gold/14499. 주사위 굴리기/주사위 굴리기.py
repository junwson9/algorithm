N,M,x,y,K = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
dice = [0,0,0,0,0,0]
di = [0,0,-1,1]
dj = [1,-1,0,0] #동서북남


for d in order:
    nx, ny = x+di[d-1], y+dj[d-1]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    top, back, right, left, front, bottom = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if d == 1:  # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = left, back, top, bottom, front, right
    elif d == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = right, back, bottom, top, front, left
    elif d == 3:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = front, top, right, left, bottom, back
    else:   #남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = back, bottom, right, left, top, front

    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[5]
    else:
        dice[5] = arr[nx][ny]
        arr[nx][ny] = 0

    x,y = nx, ny
    print(dice[0])