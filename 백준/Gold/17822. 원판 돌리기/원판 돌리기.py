import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline
N,M,T = map(int, input().split())
arr = [[0]*M]+[deque(map(int, input().split())) for _ in range(N)]

def rotate(x,d,k):
    i = x
    while True:
        if i > N:
            break
        rot = arr[i]
        if d == 0:
            for _ in range(k):
                t = arr[i].pop()
                arr[i].appendleft(t)
        if d == 1:
            for _ in range(k):
                t = arr[i].popleft()
                arr[i].append(t)
        i += x
def check(copy_arr):
    flag = 0
    for j in range(M):
        if arr[1][j] == arr[2][j] and arr[1][j] != 0:
            flag = 1
            copy_arr[1][j] = 0
            copy_arr[2][j] = 0
        if arr[1][j] == arr[1][(j+1)%M] and arr[1][j] != 0:
            flag = 1
            copy_arr[1][j] = 0
            copy_arr[1][(j+1)%M] = 0
        if arr[1][j] == arr[1][(j-1)%M] and arr[1][j] != 0:
            flag = 1
            copy_arr[1][j] = 0
            copy_arr[1][(j-1)%M] = 0

        if arr[N][j] == arr[N-1][j] and arr[N][j] != 0:
            flag = 1
            copy_arr[N][j] = 0
            copy_arr[N-1][j] = 0
        if arr[N][j] == arr[N][(j+1)%M] and arr[N][j] != 0:
            flag = 1
            copy_arr[N][j] = 0
            copy_arr[N][(j+1)%M] = 0
        if arr[N][j] == arr[N][(j-1)%M] and arr[N][j] != 0:
            flag = 1
            copy_arr[N][j] = 0
            copy_arr[N][(j-1)%M] = 0

    for i in range(2,N):
        for j in range(M):
            if arr[i][j] == arr[i][(j+1)%M] and arr[i][j] != 0:
                flag = 1
                copy_arr[i][j] = 0
                copy_arr[i][(j+1)%M] = 0
            if arr[i][j] == arr[i][(j-1)%M] and arr[i][j] != 0:
                flag = 1
                copy_arr[i][j] = 0
                copy_arr[i][(j-1)%M] = 0

            if arr[i-1][j] == arr[i][j] and arr[i][j] != 0:
                flag = 1
                copy_arr[i-1][j] = 0
                copy_arr[i][j] = 0

            if arr[i+1][j] == arr[i][j] and arr[i][j] != 0:
                flag = 1
                copy_arr[i+1][j] = 0
                copy_arr[i][j] = 0
    if flag == 0:
        copy_arr = recycle(copy_arr)
    return copy_arr

def recycle(copy_arr):
    sm = 0
    cnt = 0
    for i in range(1,N+1):
        for j in range(M):
            if arr[i][j] > 0:
                sm += copy_arr[i][j]
                cnt += 1
    if cnt == 0:
        return copy_arr
    tmp = sm/cnt
    for i in range(1,N+1):
        for j in range(M):
            if copy_arr[i][j] < tmp and copy_arr[i][j] != 0:
                copy_arr[i][j] += 1
            elif copy_arr[i][j] > tmp and copy_arr[i][j] != 0:
                copy_arr[i][j] -= 1
    return copy_arr


for _ in range(T):
    x,d,k = map(int, input().split())
    rotate(x,d,k)
    copy_arr = deepcopy(arr)
    check(copy_arr)
    arr = copy_arr
ans = 0
for i in range(1,N+1):
    for j in range(M):
        ans += arr[i][j]
print(ans)
