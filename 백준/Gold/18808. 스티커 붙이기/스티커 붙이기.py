import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
board = [[0]*m for _ in range(n)]
stickers = []

def rotate(sticker):
    r = len(sticker)
    c = len(sticker[0])
    tmp = [[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            tmp[j][r-i-1] = sticker[i][j]
    return tmp

def check(x,y,sticker):
    r = len(sticker)
    c = len(sticker[0])
    for nx in range(r):
        for ny in range(c):
            if board[x+nx][y+ny] and sticker[nx][ny]:
                return False
    return True

def stick(sticker):
    r = len(sticker)
    c = len(sticker[0])
    for x in range(n-r+1):
        for y in range(m-c+1):
            if check(x,y,sticker):
                for nx in range(r):
                    for ny in range(c):
                        board[x+nx][y+ny] += sticker[nx][ny]
                return True
    return False

for _ in range(k):
    r,c = map(int,input().split())
    sticker = [list(map(int,input().split())) for _ in range(r)]
    stickers.append(sticker)

for sticker in stickers:
    for i in range(4):
        if stick(sticker):
            break
        sticker = rotate(sticker)
ans = 0
for lst in board:
    ans += sum(lst)
print(ans)








