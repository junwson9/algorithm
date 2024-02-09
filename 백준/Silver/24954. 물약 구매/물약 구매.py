import sys
from copy import deepcopy
input = sys.stdin.readline
N = int(input())
lst = [0]+list(map(int,input().split()))
arr = [[] for _ in range(N+1)]
for i in range(1,N+1):
    pi = int(input())
    if pi == 0:
        continue
    else:
        for j in range(pi):
            arr[i].append(list(map(int,input().split())))

v = [0]*(N+1)
ans = sum(lst)
def dfs(n,tmp):
    global ans
    if n == N:
        sm = 0
        tmp_lst = deepcopy(lst)
        for i in range(N):
            sm += tmp_lst[tmp[i]]
            for j in range(len(arr[tmp[i]])):
                if tmp_lst[arr[tmp[i]][j][0]] - arr[tmp[i]][j][1] <= 0:
                    tmp_lst[arr[tmp[i]][j][0]] = 1
                else:
                    tmp_lst[arr[tmp[i]][j][0]] -= arr[tmp[i]][j][1]
        if sm < ans:
            ans = sm
        return

    for i in range(1,N+1):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1,tmp+[i])
            v[i] = 0

dfs(0,[])
print(ans)