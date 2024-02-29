import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
bullet = list(map(int,input().split()))
per = []
tmp = []
def dfs(n):
    if n == K:
        per.append(tmp[:])
        return

    for i in range(N):
        tmp.append(i)
        dfs(n+1)
        tmp.pop()
dfs(0)
di = [-1,0,1,0]
dj = [0,-1,0,1]
def shoot(lst):
    flag = 1
    cnt = 0
    copy_arr = [i[:] for i in arr]
    for i in range(len(lst)):
        for j in range(N):
            if copy_arr[lst[i]][j] >= 1:
                if copy_arr[lst[i]][j] >= 10:
                    cnt += copy_arr[lst[i]][j]
                    copy_arr[lst[i]][j] = 0
                    break
                tmp = copy_arr[lst[i]][j]-bullet[i]
                if tmp <= 0:
                    if flag == 1:
                        cnt += copy_arr[lst[i]][j]
                    else:
                        cnt += arr[lst[i]][j]
                    for k in range(4):
                        ni = lst[i]+di[k]
                        nj = j+dj[k]
                        if 0<= ni < N and 0<= nj < N:
                            if copy_arr[ni][nj] == 0:
                                copy_arr[ni][nj] = copy_arr[lst[i]][j]//4
                    copy_arr[lst[i]][j] = 0
                    flag = 1

                else:
                    copy_arr[lst[i]][j] = tmp
                    flag = 0
                break
    return cnt


ans = 0
for p in range(len(per)):
    ans = max(ans,shoot(per[p]))
print(ans)
