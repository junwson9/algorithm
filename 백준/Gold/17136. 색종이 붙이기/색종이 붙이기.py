import sys

input = sys.stdin.readline

paper = [5,5,5,5,5]
arr = [list(map(int,input().split())) for _ in range(10)]
ans = 26

def check(x,y,nx,ny):
    for i in range(x,nx+1):
        for j in range(y,ny+1):
            if arr[i][j] == 0:
                return False
    return True


def cover(x,y,nx,ny,flag):
    for i in range(x,nx+1):
        for j in range(y,ny+1):
            arr[i][j] = flag

def dfs(n):
    global ans
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                for l in range(5):
                    ni,nj = i+l,j+l
                    if paper[l] and 0<=ni<10 and 0<=nj<10:
                        if check(i,j,ni,nj):
                            paper[l] -= 1
                            cover(i,j,ni,nj,0)
                            dfs(n+1)
                            paper[l] += 1
                            cover(i,j,ni,nj,1)
                return
    ans = min(ans,n)

dfs(0)
if ans == 26:
    ans = -1
    print(ans)
else:
    print(ans)
