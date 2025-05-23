import sys

input = sys.stdin.readline
arr = [list(map(int,input().split())) for _ in range(9)]
N = 0
lst = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            N+=1
            lst.append([i,j])

def chk1(row,n):
    for col in range(9):
        if arr[row][col] == n:
            return False
    return True

def chk2(col,n):
    for row in range(9):
        if arr[row][col] == n:
            return False
    return True

def chk3(row,col,n):
    row = row//3*3
    col = col//3*3
    for i in range(3):
        for j in range(3):
            if arr[row+i][col+j] == n:
                return False
    return True

def dfs(n):
    if n == N:
        for l in arr:
            print(*l)
        exit(0)

    row = lst[n][0]
    col = lst[n][1]
    for num in range(1,10):
        if chk1(row,num) and chk2(col,num) and chk3(row,col,num):
            arr[row][col] =  num
            dfs(n+1)
            arr[row][col] = 0

dfs(0)


