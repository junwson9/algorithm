N = int(input())
arr = [[0]*101 for _ in range(101)]
di = [0,-1,0,1]
dj = [1,0,-1,0]
for _ in range(N):
    x,y,d,g = map(int, input().split())
    arr[y][x] = 1
    dragon = [d]
    for _ in range(g):
        for k in range(len(dragon)-1,-1,-1):
            dragon.append((dragon[k]+1)%4)

    for i in range(len(dragon)):
        y += di[dragon[i]]
        x += dj[dragon[i]]
        if x<0 or x> 100 or y<0 or y > 100:
            continue
        arr[y][x] = 1
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j] == 1 and arr[i+1][j+1] == 1:
            ans += 1
print(ans)



