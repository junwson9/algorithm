import sys
input = sys.stdin.readline
N,M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
def get_exist():
    global exist
    exist = [[False]*N for _ in range(N)]
    for x,y in cloud:
        exist[x][y] = True
def move(d,s):
    for i in range(len(cloud)):
        x = cloud[i][0]
        y = cloud[i][1]
        for j in range(s):
            x = (x+dx[d]+N)%N
            y = (y+dy[d]+N)%N
        cloud[i][0] = x
        cloud[i][1] = y
    get_exist()

def rain():
    for i in range(N):
        for j in range(N):
            if exist[i][j]:
                arr[i][j] += 1


def watercopy():
    copy_arr = [i[:] for i in arr]
    for i in range(N):
        for j in range(N):
            if not exist[i][j]:
                continue
            for di,dj in ((1,1),(-1,-1),(1,-1),(-1,1)):
                ni,nj = i+di,j+dj
                if 0<=ni<N and 0<=nj<N:
                    if copy_arr[ni][nj] != 0:
                        arr[i][j] += 1

def cloudagain():
    global cloud
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not exist[i][j]:
                new_cloud.append([i,j])
                arr[i][j] -= 2
    cloud = new_cloud
    get_exist()



exist = [[False]*N for _ in range(N)]
cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]


for _ in range(M):
    d,s = map(int, input().split())
    move(d,s)
    rain()
    watercopy()
    cloudagain()

ans = 0
for i in range(N):
    for j in range(N):
        ans += arr[i][j]
print(ans)