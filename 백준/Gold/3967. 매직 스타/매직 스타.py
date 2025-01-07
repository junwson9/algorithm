import sys
input = sys.stdin.readline

arr = [list(input().strip()) for _ in range(5)]
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L']
stars = []
v = [0]*12
N = 0

def check():
    if (ord(arr[0][4]) - ord('A') + 1) + (ord(arr[1][3]) - ord('A') + 1) + (ord(arr[2][2]) - ord('A') + 1) + (ord(arr[3][1]) - ord('A') + 1) != 26:
        return False
    if (ord(arr[0][4]) - ord('A') + 1) + (ord(arr[1][5]) - ord('A') + 1) + (ord(arr[2][6]) - ord('A') + 1) + (ord(arr[3][7]) - ord('A') + 1) != 26:
        return False
    if (ord(arr[1][1]) - ord('A') + 1) + (ord(arr[1][3]) - ord('A') + 1) + (ord(arr[1][5]) - ord('A') + 1) + (ord(arr[1][7]) - ord('A') + 1) != 26:
        return False
    if (ord(arr[3][1]) - ord('A') + 1) + (ord(arr[3][3]) - ord('A') + 1) + (ord(arr[3][5]) - ord('A') + 1) + (ord(arr[3][7]) - ord('A') + 1) != 26:
        return False
    if (ord(arr[4][4]) - ord('A') + 1) + (ord(arr[3][3]) - ord('A') + 1) + (ord(arr[2][2]) - ord('A') + 1) + (ord(arr[1][1]) - ord('A') + 1) != 26:
        return False
    if (ord(arr[4][4]) - ord('A') + 1) + (ord(arr[3][5]) - ord('A') + 1) + (ord(arr[2][6]) - ord('A') + 1) + (ord(arr[1][7]) - ord('A') + 1) != 26:
        return False
    return True

for i in range(5):
    for j in range(9):
        if arr[i][j] == 'x':
            stars.append([i,j])
            N += 1
        if arr[i][j] in alpha:
            v[alpha.index(arr[i][j])] = 1


def dfs(n,idx):
    if n == N:
        if check():
            for row in arr:
                print(''.join(row))
            sys.exit(0)


    for i in range(12):
        if v[i] == 0:
            v[i] = 1
            x,y = stars[idx]
            arr[x][y] = chr(i+ord('A'))
            dfs(n+1,idx+1)
            arr[x][y] = 'x'
            v[i] = 0


dfs(0,0)
