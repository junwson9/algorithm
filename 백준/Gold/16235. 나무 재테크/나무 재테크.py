import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
land = [[5]*N for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]
change = []
lst = []
for _ in range(M):
    x,y,z = map(int, input().split())
    tree[x-1][y-1].append(z)

def ss():
    for i in range(N):
        for j in range(N):
            cnt = len(tree[i][j])
            for k in range(cnt):
                if land[i][j] >= tree[i][j][k]:
                    land[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    for _ in range(k,cnt):
                        tmp = tree[i][j].pop()//2
                        land[i][j] += tmp
                    break




def autumn():
    for i in range(N):
        for j in range(N):
            cnt = len(tree[i][j])
            for k in range(cnt):
                if tree[i][j][k] % 5 == 0:
                    for di,dj in ((1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                        ni,nj = i+di,j+dj
                        if 0<=ni<N and 0<=nj<N:
                            tree[ni][nj].appendleft(1)

def winter():
    for i in range(N):
        for j in range(N):
            land[i][j] += arr[i][j]


for _ in range(K):
    ss()
    autumn()
    winter()
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)


