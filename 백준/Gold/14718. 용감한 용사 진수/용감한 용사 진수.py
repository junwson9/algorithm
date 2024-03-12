import sys
from itertools import combinations
input = sys.stdin.readline
N,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 1e9
for i in range(N):
    for j in range(N):
        for k in range(N):
            cnt = 0
            for n in range(N):
                if arr[i][0] >= arr[n][0] and arr[j][1] >= arr[n][1] and arr[k][2] >= arr[n][2]:
                    cnt += 1
            if cnt >= K:
                ans = min(ans,arr[i][0]+arr[j][1]+arr[k][2])
print(ans)