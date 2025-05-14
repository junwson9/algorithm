import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
board = [[],[]]
v1 = [0]*2*N
v2 = [0]*2*N

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            if (i+j)%2:
                board[0].append([i,j])
            else:
                board[1].append([i,j])

black = white = 0
def dfs(n,cnt,color):
    global black,white
    if n == len(board[color]):
        if color == 0:
            if cnt > black:
                black = cnt
        else:
            if cnt > white:
                white = cnt
        return

    i,j = board[color][n]
    if v1[i+j] == 0 and v2[i-j+N-1] == 0:
        v1[i+j] = v2[i-j+N-1] = 1
        dfs(n+1,cnt+1,color)
        v1[i+j] = v2[i-j+N-1] = 0
    dfs(n+1,cnt,color)

dfs(0,0,0)
dfs(0,0,1)

print(black+white)


