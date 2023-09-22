import sys
input = sys.stdin.readline
def cut(x,y,n):
    global white,blue
    color = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j] != color:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return 
    if color == 1:
        blue += 1
    if color == 0:
        white += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0
cut(0,0,N)
print(white)
print(blue)