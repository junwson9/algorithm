import sys
input = sys.stdin.readline
arr = [list(map(int ,input().split())) for _ in range(9)]
N = 0
tmp = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            N += 1
            tmp.append((i,j))

def check1(j,n):
    for k in range(9):
        if n == arr[k][j]:
            return False
    return True

def check2(i,n):
    for k in range(9):
        if n == arr[i][k]:
            return False
    return True

def check3(i,j,n):
    i = i//3*3
    j = j//3*3
    for x in range(3):
        for y in range(3):
            if arr[i+x][j+y] == n:
                return False
    return True

def dfs(n):
    if n == N:
        for lst in arr:
            print(*lst)
        exit(0)
    i = tmp[n][0]
    j = tmp[n][1]
    for num in range(1,10):
        if check1(j,num) and check2(i,num) and check3(i,j,num):
            arr[i][j] = num
            dfs(n+1)
            arr[i][j] = 0
dfs(0)

