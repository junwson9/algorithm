import sys
input = sys.stdin.readline

arr = [list(map(int,input().split())) for _ in range(3)]
rlt = 1e9
v = [0]*10
sq = [[0]*3 for _ in range(3)]


def is_valid():

    for i in range(3):
        sm = sq[i][0]+sq[i][1]+sq[i][2]
        sm2 = sq[0][i]+sq[1][i]+sq[2][i]
        if sm != 15 or sm2 != 15:
            return False

    if sq[0][0]+sq[1][1]+sq[2][2] != 15:
        return False

    if sq[0][2]+sq[1][1]+sq[2][0] != 15:
        return False
    return True

def calc():
    sm = 0
    for i in range(3):
        for j in range(3):
          sm += abs(arr[i][j]-sq[i][j])
    return sm

def dfs(n):
    global rlt
    if n == 9:
        if is_valid():
            rlt = min(rlt,calc())
            return

    row = n//3
    col = n%3

    for i in range(1,10):
        if v[i] == 0:
            sq[row][col] = i
            v[i] = 1
            dfs(n+1)
            v[i] = 0

dfs(0)
print(rlt)